#!/usr/bin/env python3
"""Valida el repositorio maestro sin red ni dependencias externas (Python 3.11+).

Uso desde la raíz del proyecto::

    python scripts/validate.py
    python scripts/validate.py --json
    python scripts/validate.py --root /otra/copia --report /tmp/validacion.json

El código de salida es 0 si la estructura es válida y 1 si hay errores. Una
validación estructural correcta no certifica calidad pedagógica ni aprendizaje.
Por defecto no se escribe ningún archivo. ``--report`` guarda el mismo informe
JSON que puede consultarse mediante ``--json``.
"""

from __future__ import annotations

import argparse
from datetime import date
from graphlib import CycleError, TopologicalSorter
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import parse_qs, unquote, urlsplit


LEVELS = [
    "exploracion", "fundamentos", "aplicacion_acompanada", "autonomia",
    "profundizacion", "creacion_investigacion",
]
CANONICAL = {
    "programs": ("catalog/programs.json", "programs"),
    "pending": ("catalog/pending.json", "items"),
    "competencies": ("competencies/competencies.json", "competencies"),
    "support": ("support/resources.json", "resources"),
    "rubrics": ("assessment/rubrics.json", "rubrics"),
    "curricula": ("curricula/mallas.json", "curricula"),
}
IGNORE_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache", "private", "exports"}
LIFE_CONTEXTS = {
    "primera_infancia", "basica", "media", "formacion_especializada",
    "vida_laboral", "reconversion", "aprendizaje_personal", "transmision_experiencia",
}
LLE_ROUTES = ["inicio", "mallas", "programas", "competencias", "apoyos", "evaluacion", "documentos"]
LLE_DETAIL_ROUTES = {
    "programa": "programs", "competencia": "competencies", "malla": "curricula",
    "apoyo": "support", "rubrica": "rubrics",
}
ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$")


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Clave JSON duplicada: {key}")
        result[key] = value
    return result


def _reject_constant(value):
    raise ValueError(f"Constante no válida en JSON: {value}")


class _HTMLInspector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors = set()
        self.links = []
        self.metadata = {}

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "meta" and attributes.get("name"):
            self.metadata[attributes["name"]] = attributes.get("content", "")
        for key in ("id", "name" if tag == "a" else "id"):
            if attributes.get(key):
                self.anchors.add(attributes[key])
        for key in ("href", "src", "poster"):
            if attributes.get(key):
                self.links.append((attributes[key], self.getpos()[0]))
        if attributes.get("srcset") and not attributes["srcset"].startswith("data:"):
            for candidate in attributes["srcset"].split(","):
                if candidate.strip():
                    self.links.append((candidate.strip().split()[0], self.getpos()[0]))


def _without_code(text):
    """Conserva líneas y encabezados; excluye bloques de código y código inline."""
    result = []
    fence = None
    for line in text.splitlines(keepends=True):
        start = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence:
            if re.match(r"^\s{0,3}" + re.escape(fence[0]) + "{" + str(fence[1]) + r",}\s*$", line):
                fence = None
            result.append("\n" if line.endswith("\n") else "")
        elif start:
            fence = (start[1][0], len(start[1]))
            result.append("\n" if line.endswith("\n") else "")
        elif line.startswith("    ") or line.startswith("\t"):
            result.append("\n" if line.endswith("\n") else "")
        else:
            result.append(line)
    return "".join(result)


def _slug(heading):
    heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading)
    heading = unescape(re.sub(r"<[^>]+>", "", heading)).strip().lower()
    heading = heading.replace("`", "").replace("*", "")
    heading = re.sub(r"(?<!\w)_{1,2}|_{1,2}(?!\w)", "", heading)
    heading = "".join(
        char for char in heading
        if char in " -_" or unicodedata.category(char)[0] in "LMN"
    )
    return heading.replace(" ", "-")


def _markdown_anchors(text):
    """Aproxima los slugs de GitHub, incluidos acentos y títulos repetidos."""
    stripped = _without_code(text)
    inspector = _HTMLInspector()
    inspector.feed(stripped)
    anchors = set(inspector.anchors)
    counts = {}
    lines = stripped.splitlines()
    for index, line in enumerate(lines):
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)(?:\s+#+\s*)?$", line)
        heading = match[1] if match else None
        if heading is None and index + 1 < len(lines) and line.strip():
            if re.match(r"^\s{0,3}(?:={3,}|-{3,})\s*$", lines[index + 1]):
                heading = line.strip()
        if heading is not None:
            base = _slug(heading)
            duplicate = counts.get(base, 0)
            anchor = base if duplicate == 0 else f"{base}-{duplicate}"
            while anchor in anchors:
                duplicate += 1
                anchor = f"{base}-{duplicate}"
            counts[base] = duplicate + 1
            anchors.add(anchor)
    return anchors


def _portal_slug(value):
    """Normalización del lector local, distinta de los anchors Markdown de GitHub."""
    value = unicodedata.normalize("NFD", value)
    value = "".join(char for char in value if not "\u0300" <= char <= "\u036f").lower()
    value = re.sub(r"\s+", " ", value).strip()
    value = "".join(char for char in value if char.isspace() or char in "_-" or unicodedata.category(char)[0] in "LN")
    return re.sub(r"\s+", "-", value.strip())


def _portal_document_anchors(text):
    anchors, counts = set(), {}
    for line in _without_code(text).splitlines():
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*$", line)
        if heading:
            base = _portal_slug(heading[2]) or "seccion"
            duplicate = counts.get(base, 0)
            anchors.add(base if not duplicate else f"{base}-{duplicate}")
            counts[base] = duplicate + 1
    return anchors


def _destination(raw):
    raw = raw.strip()
    if raw.startswith("<"):
        end = raw.find(">")
        return raw[1:end] if end >= 0 else raw[1:]
    # También admite espacios en nombres locales y títulos Markdown opcionales.
    raw = re.sub(r'''\s+(?:"[^"\n]*"|'[^'\n]*')\s*$''', "", raw)
    return re.sub(r"\\([() ])", r"\1", raw).strip()


class Validator:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.errors = []
        self.documents = {}
        self.records = {}
        self.ids = {}
        self.global_ids = {}
        self.anchor_cache = {}
        self.router_cache = {}
        self.counts = {"canonical_files": 0, "markdown_files": 0, "html_files": 0,
                       "local_links": 0, "external_urls": 0}

    def error(self, code, location, message):
        self.errors.append({"code": code, "location": str(location).replace(str(self.root), "."),
                            "message": message.replace(str(self.root), ".")})

    def text(self, record, field, location, *, empty=False):
        value = record.get(field)
        if not isinstance(value, str) or (not empty and not value.strip()):
            self.error("FIELD_TYPE", f"{location}.{field}", "Se requiere un texto" + ("." if empty else " no vacío."))
            return ""
        return value

    def strings(self, record, field, location, *, nonempty=False, unique=False):
        value = record.get(field)
        where = f"{location}.{field}"
        if not isinstance(value, list):
            self.error("FIELD_TYPE", where, "Se requiere una lista de textos.")
            return []
        if nonempty and not value:
            self.error("LIST_EMPTY", where, "La lista debe contener al menos un elemento.")
        valid = []
        for index, item in enumerate(value):
            if not isinstance(item, str) or not item.strip():
                self.error("FIELD_TYPE", f"{where}[{index}]", "Se requiere un texto no vacío.")
            else:
                valid.append(item)
        if unique and len(valid) != len(set(valid)):
            self.error("DUPLICATE_VALUE", where, "La lista contiene referencias duplicadas.")
        return valid

    def objects(self, record, field, location, *, nonempty=False):
        value = record.get(field)
        where = f"{location}.{field}"
        if not isinstance(value, list):
            self.error("FIELD_TYPE", where, "Se requiere una lista de objetos.")
            return []
        if nonempty and not value:
            self.error("LIST_EMPTY", where, "La lista debe contener al menos un objeto.")
        valid = []
        for index, item in enumerate(value):
            if isinstance(item, dict):
                valid.append((item, f"{where}[{index}]"))
            else:
                self.error("FIELD_TYPE", f"{where}[{index}]", "Se requiere un objeto.")
        return valid

    def obj(self, record, field, location):
        value = record.get(field)
        if not isinstance(value, dict):
            self.error("FIELD_TYPE", f"{location}.{field}", "Se requiere un objeto.")
            return {}
        return value

    def enum(self, record, field, location, values):
        value = self.text(record, field, location)
        if value and value not in values:
            self.error("STATE_INVALID", f"{location}.{field}", f"Valor no declarado: {value}. Valores: {', '.join(values)}.")
        return value

    def identifier(self, record, location):
        value = self.text(record, "id", location)
        if value and not ID_PATTERN.fullmatch(value):
            self.error("ID_FORMAT", f"{location}.id", "Identificador no válido; use letras, números y guiones.")
        return value

    def iso_date(self, value, location, *, empty=False):
        if empty and value == "":
            return
        try:
            if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                raise ValueError
            date.fromisoformat(value)
        except (ValueError, TypeError):
            self.error("DATE_INVALID", location, "Se requiere una fecha real YYYY-MM-DD.")

    def url(self, value, location, *, empty=False):
        if empty and value == "":
            return
        self.counts["external_urls"] += 1
        try:
            if not isinstance(value, str) or not value or re.search(r"[\s<>]", value):
                raise ValueError
            parsed = urlsplit(value)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc or not parsed.hostname:
                raise ValueError
            if parsed.username or parsed.password:
                raise ValueError
            _ = parsed.port
        except (ValueError, TypeError):
            self.error("URL_INVALID", location, "Se requiere un URL HTTP(S) absoluto y bien formado, sin credenciales.")

    def document_path(self, value, location):
        if not isinstance(value, str) or not value:
            return  # text() ya registra este caso.
        decoded = unquote(value)
        path = Path(decoded)
        if (path.is_absolute() or re.match(r"^[A-Za-z]:", decoded)
                or "\\" in decoded or ".." in path.parts or "\x00" in decoded):
            self.error("PATH_UNSAFE", location, "La ruta debe ser relativa a la raíz, usar / y permanecer dentro del repositorio.")
            return
        try:
            target = (self.root / path).resolve()
            if not target.is_relative_to(self.root):
                raise ValueError
            if not target.is_file():
                self.error("PATH_MISSING", location, f"No existe el archivo: {value}.")
        except (ValueError, OSError, RuntimeError):
            self.error("PATH_UNSAFE", location, "La ruta sale del repositorio o no puede resolverse de forma segura.")

    def refs(self, record, field, location, kind, *, nonempty=False):
        values = self.strings(record, field, location, nonempty=nonempty, unique=True)
        for value in values:
            if value not in self.ids.get(kind, set()):
                self.error("REF_UNKNOWN", f"{location}.{field}", f"Referencia inexistente en {kind}: {value}.")
        return values

    def graph(self, dependencies, location):
        try:
            tuple(TopologicalSorter(dependencies).static_order())
        except CycleError as exc:
            path = " → ".join(str(item) for item in exc.args[1])
            self.error("GRAPH_CYCLE", location, f"Ciclo de prerrequisitos: {path}.")

    def load(self):
        for kind, (filename, key) in CANONICAL.items():
            self.records[kind] = []
            self.ids[kind] = set()
            source = self.root / filename
            if not source.is_file():
                self.error("FILE_MISSING", filename, "Falta un archivo canónico requerido.")
                continue
            if not source.resolve().is_relative_to(self.root):
                self.error("PATH_UNSAFE", filename, "El archivo canónico está enlazado fuera del repositorio.")
                continue
            try:
                document = json.loads(source.read_text(encoding="utf-8"), object_pairs_hook=_unique_object,
                                      parse_constant=_reject_constant)
            except (ValueError, UnicodeError, OSError) as exc:
                self.error("JSON_PARSE", filename, f"JSON UTF-8 inválido: {exc}.")
                continue
            if not isinstance(document, dict):
                self.error("JSON_TYPE", filename, "La raíz JSON debe ser un objeto.")
                continue
            self.counts["canonical_files"] += 1
            self.documents[kind] = document
            if document.get("schema_version") != "1.0":
                self.error("SCHEMA_VERSION", filename, 'schema_version debe ser "1.0".')
            for record, where in self.objects(document, key, filename, nonempty=kind != "pending"):
                self.records[kind].append((record, where))
                identifier = self.identifier(record, where)
                if identifier:
                    if identifier in self.global_ids:
                        self.error("ID_DUPLICATE", f"{where}.id", f"ID repetido {identifier}; ya aparece en {self.global_ids[identifier]}.")
                    else:
                        self.global_ids[identifier] = where
                    self.ids[kind].add(identifier)

    def validate_programs(self):
        doc = self.documents.get("programs")
        if doc is not None:
            self.text(doc, "scope_note", "catalog/programs.json")
            self.iso_date(doc.get("reviewed_on"), "catalog/programs.json.reviewed_on")
        for item, where in self.records["programs"]:
            for field in ("name", "description", "license_note"):
                self.text(item, field, where)
            repository = self.text(item, "repository", where)
            if repository and not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
                self.error("REPOSITORY_INVALID", f"{where}.repository", "Use owner/name con el nombre real del repositorio.")
            self.url(self.text(item, "url", where), f"{where}.url")
            self.enum(item, "role", where, ("programa", "laboratorio", "herramienta", "programa_y_herramienta"))
            for field in ("domains", "audiences"):
                self.strings(item, field, where, nonempty=True)
            self.refs(item, "competency_ids", where, "competencies")
            self.document_path(self.text(item, "integration_doc", where), f"{where}.integration_doc")
            review = self.obj(item, "review", where)
            review_where = f"{where}.review"
            status = self.enum(review, "status", review_where, ("readme_revisado", "indice_revisado", "pendiente"))
            self.iso_date(review.get("reviewed_on"), f"{review_where}.reviewed_on", empty=status == "pendiente")
            self.url(self.text(review, "source_url", review_where, empty=status == "pendiente"), f"{review_where}.source_url", empty=status == "pendiente")
            for field in ("content_sha", "scope", "declared_content_status"):
                self.text(review, field, review_where, empty=field == "content_sha" and status == "pendiente")
            human = review.get("human_validation")
            if not isinstance(human, (str, bool)) or (isinstance(human, str) and not human.strip()):
                self.error("FIELD_TYPE", f"{review_where}.human_validation", "Se requiere booleano o descripción explícita de la revisión humana.")
            for entry, entry_where in self.objects(item, "entry_points", where):
                self.text(entry, "label", entry_where)
                self.text(entry, "verification", entry_where)
                self.url(self.text(entry, "url", entry_where), f"{entry_where}.url")
        for item, where in self.records["pending"]:
            for field in ("topic", "known_context", "reason_pending", "next_action"):
                self.text(item, field, where)

    def validate_competencies(self):
        doc = self.documents.get("competencies")
        if doc is not None and doc.get("levels") != LEVELS:
            self.error("LEVELS_INVALID", "competencies/competencies.json.levels", "Se requieren los seis niveles declarados y en el orden del contrato.")
        dependencies = {}
        for item, where in self.records["competencies"]:
            for field in ("title", "domain", "description", "transfer_task"):
                self.text(item, field, where)
            self.enum(item, "review_status", where, ("propuesta_editorial",))
            for field in ("outcomes", "evidence"):
                self.strings(item, field, where, nonempty=True)
            self.refs(item, "program_ids", where, "programs")
            prerequisites = self.refs(item, "prerequisites", where, "competencies")
            identifier = item.get("id")
            if isinstance(identifier, str):
                dependencies[identifier] = prerequisites
            descriptors = self.obj(item, "level_descriptors", where)
            if set(descriptors) != set(LEVELS):
                self.error("LEVEL_DESCRIPTORS", f"{where}.level_descriptors", "El objeto debe contener exactamente las seis claves de nivel.")
            for level in LEVELS:
                self.text(descriptors, level, f"{where}.level_descriptors")
        self.graph(dependencies, "competencies/competencies.json.prerequisites")

    def validate_support(self):
        for item, where in self.records["support"]:
            for field in ("title", "purpose", "trigger"):
                self.text(item, field, where)
            for field in ("activities", "success_criteria"):
                self.strings(item, field, where, nonempty=True)
            self.refs(item, "program_ids", where, "programs")
            self.refs(item, "competency_ids", where, "competencies")
            self.enum(item, "status", where, ("guia_inicial",))
            self.document_path(self.text(item, "doc_path", where), f"{where}.doc_path")

    def validate_rubrics(self):
        doc = self.documents.get("rubrics")
        if doc is not None:
            values = []
            for level, where in self.objects(doc, "scale", "assessment/rubrics.json", nonempty=True):
                value = level.get("value")
                if type(value) is not int:
                    self.error("SCALE_INVALID", f"{where}.value", "El valor debe ser un entero de 0 a 3.")
                else:
                    values.append(value)
                self.text(level, "label", where)
            if sorted(values) != [0, 1, 2, 3]:
                self.error("SCALE_INVALID", "assessment/rubrics.json.scale", "La escala debe contener 0, 1, 2 y 3 exactamente una vez.")
        for item, where in self.records["rubrics"]:
            for field in ("title", "purpose", "decision_rule", "limitations"):
                self.text(item, field, where)
            self.document_path(self.text(item, "doc_path", where), f"{where}.doc_path")
            criteria_ids = set()
            for criterion, criterion_where in self.objects(item, "criteria", where, nonempty=True):
                identifier = self.identifier(criterion, criterion_where)
                if identifier and identifier in criteria_ids:
                    self.error("ID_DUPLICATE", f"{criterion_where}.id", "ID de criterio repetido dentro de la rúbrica.")
                criteria_ids.add(identifier)
                self.text(criterion, "title", criterion_where)
                descriptors = self.obj(criterion, "descriptors", criterion_where)
                if set(descriptors) != {"0", "1", "2", "3"}:
                    self.error("RUBRIC_DESCRIPTORS", f"{criterion_where}.descriptors", "Los descriptores deben tener las claves 0, 1, 2 y 3.")
                for value in ("0", "1", "2", "3"):
                    self.text(descriptors, value, f"{criterion_where}.descriptors")

    def validate_curricula(self):
        for item, where in self.records["curricula"]:
            for field in ("title", "purpose", "entry_profile", "content_readiness"):
                self.text(item, field, where)
            for field in ("audience", "life_contexts", "diagnostic", "objectives"):
                values = self.strings(item, field, where, nonempty=True)
                if field == "life_contexts":
                    for value in values:
                        if value not in LIFE_CONTEXTS:
                            self.error("CONTEXT_INVALID", f"{where}.life_contexts", f"Contexto vital no declarado: {value}.")
            for field, kind in (("entry_competencies", "competencies"), ("competency_ids", "competencies"),
                                ("program_ids", "programs"), ("support_ids", "support"), ("next_routes", "curricula")):
                self.refs(item, field, where, kind)
            self.enum(item, "status", where, ("diseno_inicial",))
            self.document_path(self.text(item, "doc_path", where), f"{where}.doc_path")
            assessment = self.obj(item, "assessment", where)
            rubric = self.text(assessment, "rubric_id", f"{where}.assessment")
            if rubric and rubric not in self.ids["rubrics"]:
                self.error("REF_UNKNOWN", f"{where}.assessment.rubric_id", f"No existe la rúbrica {rubric}.")
            for field in ("evidence", "criteria"):
                self.strings(assessment, field, f"{where}.assessment", nonempty=True)
            steps = self.objects(item, "steps", where, nonempty=True)
            step_ids = set()
            for step, step_where in steps:
                identifier = self.identifier(step, step_where)
                if identifier and identifier in step_ids:
                    self.error("ID_DUPLICATE", f"{step_where}.id", "ID de paso repetido dentro de la malla.")
                step_ids.add(identifier)
            dependencies = {}
            for step, step_where in steps:
                for field in ("title", "availability"):
                    self.text(step, field, step_where)
                for field in ("outcomes", "activities", "evidence", "acceptance_criteria", "alternatives"):
                    self.strings(step, field, step_where, nonempty=True)
                for field, kind in (("competency_ids", "competencies"), ("program_ids", "programs"), ("support_ids", "support")):
                    self.refs(step, field, step_where, kind)
                requires = self.strings(step, "requires", step_where, unique=True)
                for requirement in requires:
                    if requirement not in step_ids:
                        self.error("STEP_REF_UNKNOWN", f"{step_where}.requires", f"El paso {requirement} no pertenece a esta malla.")
                identifier = step.get("id")
                if isinstance(identifier, str):
                    dependencies[identifier] = requires
            self.graph(dependencies, f"{where}.steps.requires")
        # next_routes expresa continuidad y revisión: sus ciclos están permitidos.

    def anchors(self, target):
        if target in self.anchor_cache:
            return self.anchor_cache[target]
        try:
            text = target.read_text(encoding="utf-8")
            if target.suffix.lower() in {".md", ".markdown"}:
                anchors = _markdown_anchors(text)
            else:
                inspector = _HTMLInspector()
                inspector.feed(text)
                anchors = inspector.anchors
        except (OSError, UnicodeError, ValueError) as exc:
            self.error("TEXT_READ", target.relative_to(self.root), f"No se pudo leer el destino: {exc}.")
            anchors = set()
        self.anchor_cache[target] = anchors
        return anchors

    def router_info(self, target, inspector=None):
        """Reconoce sólo el contrato declarado del lector; no omite anchors HTML."""
        if target in self.router_cache:
            return self.router_cache[target]
        if inspector is None:
            try:
                inspector = _HTMLInspector()
                inspector.feed(target.read_text(encoding="utf-8"))
            except (OSError, UnicodeError) as exc:
                self.error("TEXT_READ", target.relative_to(self.root), f"No se pudo leer la declaración del lector: {exc}.")
                self.router_cache[target] = None
                return None
        meta = inspector.metadata
        info = None
        if "lle-router" in meta:
            where = target.relative_to(self.root)
            if meta["lle-router"] != "hash":
                self.error("ROUTER_DECLARATION", where, "lle-router debe declarar el tipo hash del lector.")
            elif meta.get("lle-routes", "").split() != LLE_ROUTES:
                self.error("ROUTER_DECLARATION", where, "lle-routes debe enumerar las siete secciones de NAV, exactamente una vez y en su orden declarado.")
            else:
                base = meta.get("lle-document-root", "")
                try:
                    relative = Path(base)
                    if (not base or relative.is_absolute() or re.match(r"^[A-Za-z]:", base)
                            or "\\" in base or (target.parent / relative).resolve() != self.root):
                        raise ValueError
                    info = {"routes": set(LLE_ROUTES), "root": self.root}
                except (ValueError, OSError, RuntimeError):
                    self.error("ROUTER_DECLARATION", where, "lle-document-root debe ser relativo al HTML y resolver a la raíz del repositorio.")
        self.router_cache[target] = info
        return info

    def router_fragment(self, target, fragment, where):
        """Devuelve None si no es ruta conocida; los errores reconocidos se registran."""
        info = self.router_info(target)
        if info is None:
            return None
        route, separator, raw_query = fragment.partition("?")
        if route in info["routes"] and not separator:
            return True
        kind, slash, identifier = route.partition("/")
        if not slash:
            return None
        if kind in LLE_DETAIL_ROUTES:
            if separator:
                self.error("ROUTER_QUERY", where, "Las vistas de entidades no declaran parámetros de consulta.")
            elif identifier not in self.ids.get(LLE_DETAIL_ROUTES[kind], set()):
                self.error("ROUTER_REF_UNKNOWN", where, f"La ruta {kind} referencia un ID inexistente: {identifier}.")
            else:
                return True
            return False
        if kind != "doc":
            return None
        path = Path(identifier)
        try:
            if (not identifier or path.is_absolute() or ".." in path.parts or "\\" in identifier
                    or "\x00" in identifier or re.match(r"^[A-Za-z]:", identifier)
                    or any(part in IGNORE_DIRS or part.startswith(".") for part in path.parts)):
                raise ValueError
            document = (info["root"] / path).resolve()
            if not document.is_relative_to(self.root):
                raise ValueError
        except (ValueError, OSError, RuntimeError):
            self.error("ROUTER_PATH", where, "La ruta de documento debe permanecer dentro del repositorio distribuido.")
            return False
        if not document.is_file() or document.suffix.lower() != ".md":
            self.error("ROUTER_DOC_MISSING", where, f"No existe el documento Markdown de la ruta: {identifier}.")
            return False
        query = parse_qs(raw_query, keep_blank_values=True)
        if set(query) - {"a"} or len(query.get("a", [])) > 1:
            self.error("ROUTER_QUERY", where, "La vista documental sólo admite un parámetro a de encabezado.")
            return False
        anchor = query.get("a", [""])[0]
        if anchor:
            try:
                anchors = _portal_document_anchors(document.read_text(encoding="utf-8"))
            except (OSError, UnicodeError) as exc:
                self.error("TEXT_READ", document.relative_to(self.root), f"No se pudo leer el documento de la ruta: {exc}.")
                return False
            if _portal_slug(anchor) not in anchors:
                self.error("ROUTER_DOC_FRAGMENT", where, f"No existe el encabezado solicitado en {identifier}: {anchor}.")
                return False
        return True

    def link(self, source, destination, line):
        destination = unescape(destination).strip()
        if not destination:
            return
        where = f"{source.relative_to(self.root)}:{line}"
        try:
            parsed = urlsplit(destination)
        except ValueError:
            self.error("LINK_INVALID", where, f"Enlace no interpretable: {destination}.")
            return
        if parsed.scheme in {"http", "https"}:
            self.url(destination, where)
            return
        if parsed.scheme or parsed.netloc:
            return  # mailto, data, app y otros esquemas no son archivos locales.
        self.counts["local_links"] += 1
        relative = unquote(parsed.path)
        if "\x00" in relative or "\\" in relative:
            self.error("LINK_UNSAFE", where, f"Ruta local no válida: {destination}.")
            return
        try:
            if relative.startswith("/"):
                target = (self.root / relative.lstrip("/")).resolve()
            else:
                target = (source.parent / relative).resolve() if relative else source.resolve()
            if not target.is_relative_to(self.root):
                self.error("LINK_UNSAFE", where, f"El enlace sale del repositorio: {destination}.")
                return
            if not target.exists():
                self.error("LINK_MISSING", where, f"No existe el destino: {destination}.")
                return
        except (OSError, ValueError, RuntimeError):
            self.error("LINK_UNSAFE", where, f"No se puede resolver el enlace: {destination}.")
            return
        if target.is_dir():
            for filename in ("README.md", "index.html"):
                if (target / filename).is_file():
                    target = target / filename
                    break
        if parsed.fragment and target.is_file() and target.suffix.lower() in {".md", ".markdown", ".html", ".htm"}:
            fragment = unquote(parsed.fragment)
            if fragment not in self.anchors(target):
                routing = self.router_fragment(target, fragment, where) if target.suffix.lower() in {".html", ".htm"} else None
                if routing is None:
                    self.error("LINK_FRAGMENT", where, f"No existe el fragmento #{fragment} en {target.relative_to(self.root)}.")

    def validate_links(self):
        # Sólo documentos del repositorio; las dependencias y metadatos de git se excluyen.
        for source in sorted(self.root.rglob("*")):
            if any(part in IGNORE_DIRS for part in source.relative_to(self.root).parts):
                continue
            if not source.is_file() or source.suffix.lower() not in {".md", ".markdown", ".html", ".htm"}:
                continue
            if not source.resolve().is_relative_to(self.root):
                self.error("LINK_UNSAFE", source.relative_to(self.root), "Documento enlazado simbólicamente fuera del repositorio.")
                continue
            try:
                original = source.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                self.error("TEXT_READ", source.relative_to(self.root), f"No se pudo leer como UTF-8: {exc}.")
                continue
            if source.suffix.lower() in {".html", ".htm"}:
                self.counts["html_files"] += 1
                inspector = _HTMLInspector()
                inspector.feed(original)
                self.router_info(source, inspector)
                for destination, line in inspector.links:
                    self.link(source, destination, line)
                continue
            self.counts["markdown_files"] += 1
            text = _without_code(original)
            text = re.sub(r"(`+)(.+?)\1", lambda match: " " * len(match[0]), text)
            definitions = {}
            for match in re.finditer(r"(?m)^\s{0,3}\[([^]\n]+)\]:\s*(.+)$", text):
                definitions[match[1].strip().casefold()] = _destination(match[2])
                self.link(source, definitions[match[1].strip().casefold()], text.count("\n", 0, match.start()) + 1)
            pattern = r"!?\[[^]\n]*\]\(\s*(<[^>\n]+>|(?:[^()\n]|\([^()\n]*\))+?)\s*\)"
            for match in re.finditer(pattern, text):
                self.link(source, _destination(match[1]), text.count("\n", 0, match.start()) + 1)
            for match in re.finditer(r"!?\[([^]\n]+)\]\[([^]\n]*)\]", text):
                label = (match[2] or match[1]).strip().casefold()
                if label not in definitions:
                    self.error("LINK_REFERENCE", f"{source.relative_to(self.root)}:{text.count(chr(10), 0, match.start()) + 1}", f"Referencia Markdown no definida: {label}.")
            inspector = _HTMLInspector()
            inspector.feed(text)
            for destination, line in inspector.links:
                self.link(source, destination, line)

    def run(self):
        if not self.root.is_dir():
            self.error("ROOT_MISSING", self.root, "La raíz debe ser un directorio existente.")
        else:
            self.load()
            self.validate_programs()
            self.validate_competencies()
            self.validate_support()
            self.validate_rubrics()
            self.validate_curricula()
            self.validate_links()
        self.counts.update({kind: len(records) for kind, records in self.records.items()})
        return {"schema_version": "1.0", "valid": not self.errors, "root": self.root.name,
                "network_used": False, "counts": self.counts, "errors": self.errors,
                "scope": "Estructura, referencias y enlaces locales. No certifica calidad pedagógica ni dominio personal."}


def validate_repository(root):
    """API sin efectos laterales: devuelve un informe serializable a JSON."""
    return Validator(root).run()


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Raíz del repositorio a validar.")
    parser.add_argument("--json", action="store_true", help="Informe JSON por stdout.")
    parser.add_argument("--report", type=Path, help="Guardar explícitamente un informe JSON en esta ruta.")
    args = parser.parse_args(argv)
    report = validate_repository(args.root)
    payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        try:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(payload, encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            print(f"No se pudo escribir el informe: {exc}", file=sys.stderr)
            return 1
    if args.json:
        print(payload, end="")
    elif report["valid"]:
        counts = report["counts"]
        print(f"VALIDACIÓN CORRECTA: {counts.get('programs', 0)} programas, {counts.get('competencies', 0)} competencias, {counts.get('curricula', 0)} mallas; {counts['local_links']} enlaces locales comprobados.")
        print("Sin consultas de red. La revisión estructural no certifica aprendizaje ni calidad pedagógica.")
    else:
        print(f"VALIDACIÓN CON ERRORES: {len(report['errors'])} problema(s).")
        for error in report["errors"]:
            print(f"[{error['code']}] {error['location']}: {error['message']}")
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
