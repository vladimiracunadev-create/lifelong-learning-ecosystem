#!/usr/bin/env python3
"""Empaqueta el repositorio y genera MANIFEST.json usando biblioteca estándar.

Uso: python scripts/package_release.py --output dist/lifelong-learning-ecosystem-v0.1.0.zip
La validación y la vigencia del lector deben comprobarse antes de invocar esta herramienta.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile

EXCLUDED_PARTS = {".git", ".venv", "__pycache__", ".pytest_cache", ".uv-cache", "private", "exports", "dist", "build", ".work"}
EXCLUDED_NAMES = {".DS_Store", "Thumbs.db", "MANIFEST.json"}


def release_files(root: Path) -> list[Path]:
    selected = []
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"No se empaquetan enlaces simbólicos: {relative.as_posix()}")
        if not path.is_file():
            continue
        if path.name in EXCLUDED_NAMES or path.suffix.lower() in {".zip", ".pyc", ".pyo"} or path.name.endswith(".local.json"):
            continue
        selected.append(path)
    return sorted(selected, key=lambda p: p.relative_to(root).as_posix())


def package(root: Path, output: Path) -> dict:
    root = root.resolve()
    output = output.resolve()
    if output.suffix.lower() != ".zip":
        raise ValueError("La salida debe usar extensión .zip.")
    if output.exists():
        raise ValueError("La salida ya existe. Elige otro nombre o retira esa copia explícitamente.")
    paths = release_files(root)
    for required in ["README.md", "PROMPT_MAESTRO.md", "index.html", "catalog/programs.json", "curricula/mallas.json"]:
        if not (root / required).is_file():
            raise ValueError(f"Falta el archivo necesario: {required}")
    records = []
    for path in paths:
        content = path.read_bytes()
        records.append({"path": path.relative_to(root).as_posix(), "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()})
    manifest = {
        "schema_version": "1.0", "project": "lifelong-learning-ecosystem", "version": "0.1.0",
        "release_date": "2026-10-05", "hash_algorithm": "SHA-256",
        "scope": "Archivos distribuidos; MANIFEST.json se excluye de su propio hash.",
        "file_count_excluding_manifest": len(records), "files": records,
    }
    manifest_path = root / "MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    paths.append(manifest_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in sorted(paths, key=lambda p: p.relative_to(root).as_posix()):
                name = "lifelong-learning-ecosystem/" + path.relative_to(root).as_posix()
                info = zipfile.ZipInfo(name, date_time=(2026, 10, 5, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
        with zipfile.ZipFile(output) as archive:
            bad = archive.testzip()
            if bad is not None:
                raise ValueError(f"Error de integridad de ZIP: {bad}")
    except BaseException:
        output.unlink(missing_ok=True)
        raise
    return {"archive": output.name, "file_count": len(paths), "bytes": output.stat().st_size, "sha256": hashlib.sha256(output.read_bytes()).hexdigest()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(package(args.root, args.output), ensure_ascii=False, indent=2))
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"No se creó el paquete: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
