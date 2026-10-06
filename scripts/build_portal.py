#!/usr/bin/env python3
"""Construye el lector local, autocontenido y determinístico del ecosistema.

Python 3.11 o posterior. Solo biblioteca estándar; no accede a la red.
Uso: python scripts/build_portal.py [--check]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import tomllib


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = {
    "programs": ("catalog/programs.json", "programs"),
    "competencies": ("competencies/competencies.json", "competencies"),
    "support": ("support/resources.json", "resources"),
    "rubrics": ("assessment/rubrics.json", "rubrics"),
    "curricula": ("curricula/mallas.json", "curricula"),
}
SKIP_DIRS = {"node_modules", "__pycache__", "dist", "build", "venv", "private", "exports"}


class BuildError(Exception):
    """Entrada incompleta o incompatible; conserva la salida anterior."""


def read_utf8(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise BuildError(f"No se puede leer {path.relative_to(ROOT)} como UTF-8: {exc}") from exc


def normalized_source_bytes(path: Path) -> bytes:
    """Normaliza saltos de línea para que la huella sea estable entre sistemas."""
    return read_utf8(path).encode("utf-8")


def read_dataset(relative: str, collection: str) -> dict:
    try:
        data = json.loads(read_utf8(ROOT / relative))
    except json.JSONDecodeError as exc:
        raise BuildError(f"JSON inválido en {relative}, línea {exc.lineno}: {exc.msg}") from exc
    if not isinstance(data, dict) or data.get("schema_version") != "1.0":
        raise BuildError(f"{relative} debe ser un objeto con schema_version: '1.0'.")
    if not isinstance(data.get(collection), list) or not data[collection]:
        raise BuildError(f"{relative} debe contener una lista '{collection}' no vacía.")
    seen: set[str] = set()
    for index, item in enumerate(data[collection]):
        if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not item["id"]:
            raise BuildError(f"{relative}: registro {index + 1} sin identificador válido.")
        if item["id"] in seen:
            raise BuildError(f"{relative}: identificador repetido {item['id']}.")
        seen.add(item["id"])
    return data


def document_paths() -> list[Path]:
    found: list[Path] = []
    for base, dirs, files in os.walk(ROOT, followlinks=False):
        dirs[:] = sorted(d for d in dirs if not d.startswith(".") and d not in SKIP_DIRS)
        for filename in sorted(files):
            path = Path(base) / filename
            if not filename.startswith(".") and path.suffix.lower() == ".md" and not path.is_symlink():
                found.append(path)
    return sorted(found, key=lambda p: p.relative_to(ROOT).as_posix())


def embedded_json(value: object) -> str:
    # El contenido de los datos nunca puede cerrar el elemento <script>.
    return (
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        .replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def generate() -> tuple[str, dict]:
    required = [relative for relative, _ in CANONICAL.values()] + ["portal/template.html"]
    missing = [relative for relative in required if not (ROOT / relative).is_file()]
    if missing:
        raise BuildError(
            "Faltan entradas obligatorias; el portal no se ha generado:\n  - "
            + "\n  - ".join(missing)
            + "\nCompleta los datos canónicos y vuelve a ejecutar este comando."
        )

    payload = {key: read_dataset(relative, collection) for key, (relative, collection) in CANONICAL.items()}
    digest_paths = [ROOT / relative for relative in required]
    digest_paths.append(Path(__file__).resolve())

    pending = ROOT / "catalog/pending.json"
    if pending.is_file():
        try:
            pending_data = json.loads(read_utf8(pending))
        except json.JSONDecodeError as exc:
            raise BuildError(f"JSON inválido en catalog/pending.json: {exc.msg}") from exc
        if not isinstance(pending_data, dict) or not isinstance(pending_data.get("items"), list):
            raise BuildError("catalog/pending.json debe contener una lista 'items'.")
        payload["pending"] = pending_data
        digest_paths.append(pending)

    documents = {}
    for path in document_paths():
        relative = path.relative_to(ROOT).as_posix()
        content = read_utf8(path)
        title = next((line[2:].strip() for line in content.splitlines() if line.startswith("# ")), path.stem)
        documents[relative] = {"title": title, "content": content}
        digest_paths.append(path)

    # Estas rutas deben ser legibles en el propio portal, no solo enlaces de intención.
    for group, collection, field in [
        ("programs", "programs", "integration_doc"),
        ("support", "resources", "doc_path"),
        ("rubrics", "rubrics", "doc_path"),
        ("curricula", "curricula", "doc_path"),
    ]:
        for item in payload[group][collection]:
            target = item.get(field)
            if not isinstance(target, str) or target not in documents:
                raise BuildError(f"{item['id']}: {field} debe apuntar a un Markdown existente; se recibió {target!r}.")

    version = "0.1.0"
    pyproject = ROOT / "pyproject.toml"
    if pyproject.is_file():
        try:
            project = tomllib.loads(read_utf8(pyproject))
            version = str(project.get("project", {}).get("version", version))
        except tomllib.TOMLDecodeError as exc:
            raise BuildError(f"pyproject.toml inválido: {exc}") from exc
        digest_paths.append(pyproject)

    digest = hashlib.sha256()
    for path in sorted(set(digest_paths), key=lambda p: p.relative_to(ROOT).as_posix()):
        digest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        digest.update(b"\x00")
        digest.update(normalized_source_bytes(path))
        digest.update(b"\x00")
    info = {
        "version": version,
        "source_sha256": digest.hexdigest(),
        "counts": {
            "programs": len(payload["programs"]["programs"]),
            "competencies": len(payload["competencies"]["competencies"]),
            "curricula": len(payload["curricula"]["curricula"]),
            "support": len(payload["support"]["resources"]),
            "rubrics": len(payload["rubrics"]["rubrics"]),
            "documents": len(documents),
        },
    }

    template = read_utf8(ROOT / "portal/template.html")
    root_meta = '<meta name="lle-document-root" content="..">'
    if template.count(root_meta) != 1:
        raise BuildError("La plantilla debe declarar exactamente una raíz de documentos '..'.")
    template = template.replace(root_meta, '<meta name="lle-document-root" content=".">')
    replacements = {
        "__PORTAL_DATA__": embedded_json(payload),
        "__PORTAL_DOCS__": embedded_json(documents),
        "__PORTAL_BUILD__": embedded_json(info),
    }
    for marker, value in replacements.items():
        if template.count(marker) != 1:
            raise BuildError(f"portal/template.html debe incluir exactamente un marcador {marker}.")
        template = template.replace(marker, value)
    return template.rstrip() + "\n", info


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="Comprueba que index.html coincide exactamente con las fuentes, sin escribir.")
    args = parser.parse_args()
    try:
        expected, info = generate()
        destination = ROOT / "index.html"
        encoded = expected.encode("utf-8")
        if args.check:
            if not destination.is_file() or destination.read_bytes() != encoded:
                print("Portal ausente o desactualizado. Ejecuta: python scripts/build_portal.py", file=sys.stderr)
                return 1
            action = "Portal vigente"
        else:
            temp_name = None
            try:
                with tempfile.NamedTemporaryFile(mode="wb", dir=ROOT, prefix=".portal-", suffix=".tmp", delete=False) as handle:
                    temp_name = handle.name
                    handle.write(encoded)
                os.replace(temp_name, destination)
            finally:
                if temp_name and Path(temp_name).exists():
                    Path(temp_name).unlink()
            action = "Portal generado: index.html"
        counts = info["counts"]
        print(
            f"{action} | {counts['curricula']} mallas · {counts['programs']} programas · "
            f"{counts['competencies']} competencias · {counts['support']} apoyos · "
            f"{counts['rubrics']} rúbricas · {counts['documents']} documentos | {len(encoded):,} bytes"
        )
        return 0
    except (BuildError, OSError) as exc:
        print(f"Error de construcción: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
