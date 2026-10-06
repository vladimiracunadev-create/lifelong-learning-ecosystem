#!/usr/bin/env python3
"""Exporta una malla a un plan Markdown editable y ficticio, sin datos personales.

Uso::

    python scripts/export_plan.py --route M-03 --output /ruta/plan-M-03.md
    python scripts/export_plan.py --route M-03 --output plan.md --root /otra/copia

La malla y sus referencias se validan antes de exportar. El archivo resultante
no acredita dominio: todos los resultados personales empiezan sin evaluar.
No se realizan peticiones de red. Una exportación previa sólo se reemplaza si
se indica ``--force``; los seis archivos JSON canónicos nunca se sobrescriben.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from validate import CANONICAL, validate_repository


def _bullets(values):
    return "\n".join(f"- {value}" for value in values) if values else "Sin requisitos declarados."


def _table_text(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_plan(root, route_id):
    """Genera el texto; el llamador es responsable de validar y elegir destino."""
    root = Path(root)
    curricula = json.loads((root / "curricula/mallas.json").read_text(encoding="utf-8"))["curricula"]
    programs = {item["id"]: item for item in json.loads((root / "catalog/programs.json").read_text(encoding="utf-8"))["programs"]}
    competencies = {item["id"]: item for item in json.loads((root / "competencies/competencies.json").read_text(encoding="utf-8"))["competencies"]}
    support = {item["id"]: item for item in json.loads((root / "support/resources.json").read_text(encoding="utf-8"))["resources"]}
    rubrics = {item["id"]: item for item in json.loads((root / "assessment/rubrics.json").read_text(encoding="utf-8"))["rubrics"]}
    routes = {item["id"]: item for item in curricula}
    if route_id not in routes:
        raise ValueError(f"No existe la malla {route_id}. Disponibles: {', '.join(routes)}")
    route = routes[route_id]
    rubric = rubrics[route["assessment"]["rubric_id"]]
    program_names = lambda ids: ", ".join(f"{value} — {programs[value]['name']}" for value in ids) or "Sin programa externo asignado."
    competency_names = lambda ids: [f"{value} — {competencies[value]['title']}" for value in ids]
    lines = [
        f"# Plan editable — {route['title']}", "",
        f"**Malla de origen:** {route_id} · **Estado del diseño:** {route['status']}", "",
        "**Perfil:** ejemplo ficticio sin datos personales. **Estado personal inicial:** sin evaluar.", "",
        "Este documento organiza una propuesta de aprendizaje. Marcar actividades realizadas no acredita competencias; el dominio requiere revisar evidencias con criterios explícitos. Las decisiones siguen pendientes hasta esa revisión.", "",
        "## Mi objetivo y condiciones", "",
        "- Objetivo personal: ____________________",
        "- Experiencia o evidencias previas que quiero revisar: ____________________",
        "- Recursos y acompañamiento disponibles: ____________________",
        "- Preferencias de acceso y apoyos: ____________________",
        "- Dedicación elegida por la persona: ____________________",
        "- Fecha o condición de revisión del plan: ____________________", "",
        "## Propósito y punto de entrada", "", route["purpose"], "",
        f"**Perfil de ingreso propuesto:** {route['entry_profile']}", "",
        f"**Destinatarios:** {', '.join(route['audience'])}", "",
        f"**Contextos orientativos:** {', '.join(route['life_contexts'])}. Estos filtros no son barreras de edad.", "",
        f"**Disponibilidad real:** {route['content_readiness']}", "",
        "### Competencias de entrada por revisar", "", _bullets(competency_names(route["entry_competencies"])), "",
        "### Tareas de diagnóstico", "", _bullets(route["diagnostic"]), "",
        "**Decisión de ingreso pendiente:** comenzar en el inicio / revisar evidencias previas / incorporar un apoyo / adaptar el recorrido.", "",
        "## Resultados y competencias", "", _bullets(route["objectives"]), "",
        _bullets(competency_names(route["competency_ids"])), "",
        "## Secuencia de trabajo", "",
        "Las dependencias describen el orden necesario. Los tiempos se acuerdan según las condiciones y el progreso observado.", "",
    ]
    for step in route["steps"]:
        lines.extend([
            f"### {step['id']} — {step['title']}", "",
            f"**Pasos previos:** {', '.join(step['requires']) if step['requires'] else 'Ninguno dentro de esta malla.'}", "",
            f"**Programas vinculados:** {program_names(step['program_ids'])}", "",
            f"**Disponibilidad:** {step['availability']}", "",
            "**Resultados esperados:**", "", _bullets(step["outcomes"]), "",
            "**Competencias relacionadas:**", "", _bullets(competency_names(step["competency_ids"])), "",
            "**Actividades propuestas:**", "", _bullets(step["activities"]), "",
            "**Evidencias que se solicitarán:**", "", _bullets(step["evidence"]), "",
            "**Criterios para revisar las evidencias:**", "", _bullets(step["acceptance_criteria"]), "",
            "**Alternativas y adaptación:**", "", _bullets(step["alternatives"]), "",
            "**Apoyos vinculados:**", "", _bullets([f"{key} — {support[key]['title']}: {support[key]['purpose']}" for key in step["support_ids"]]), "",
            "**Registro personal pendiente:**", "",
            "- [ ] Se realizó la actividad; esta marca no acredita dominio.",
            "- Evidencia producida y ubicación privada: ____________________",
            "- Observaciones del aprendiz: ____________________",
            "- Retroalimentación recibida: ____________________",
            "- Decisión de revisión: sin evaluar.", "",
        ])
    lines.extend([
        "## Evaluación y revisión", "",
        f"**Rúbrica:** {rubric['id']} — {rubric['title']}", "", rubric["purpose"], "",
        "**Evidencias de la malla:**", "", _bullets(route["assessment"]["evidence"]), "",
        "**Criterios de la malla:**", "", _bullets(route["assessment"]["criteria"]), "",
        "| Criterio | 0 | 1 | 2 | 3 |", "| --- | --- | --- | --- | --- |",
    ])
    for criterion in rubric["criteria"]:
        cells = [criterion["title"]] + [criterion["descriptors"][str(value)] for value in range(4)]
        lines.append("| " + " | ".join(_table_text(cell) for cell in cells) + " |")
    lines.extend([
        "", f"**Regla de decisión:** {rubric['decision_rule']}", "",
        f"**Límites de interpretación:** {rubric['limitations']}", "",
        "**Resultado personal:** sin evaluar. Los números anteriores son descriptores de la rúbrica; no son puntuaciones asignadas a la persona.", "",
        "## Recursos y apoyos", "",
    ])
    linked_programs = list(dict.fromkeys(route["program_ids"] + [key for step in route["steps"] for key in step["program_ids"]]))
    for key in linked_programs:
        item = programs[key]
        lines.extend([f"- [{item['name']}]({item['url']}) ({key}). Alcance de revisión: {item['review']['scope']}"])
    linked_support = list(dict.fromkeys(route["support_ids"] + [key for step in route["steps"] for key in step["support_ids"]]))
    for key in linked_support:
        item = support[key]
        lines.extend(["", f"### {key} — {item['title']}", "", item["purpose"], "",
                      f"**Cuándo usarlo:** {item['trigger']}", "", _bullets(item["activities"]), "",
                      "**Criterios de revisión del apoyo:**", "", _bullets(item["success_criteria"])])
    lines.extend(["", "## Continuidad", "", _bullets([f"{key} — {routes[key]['title']}" for key in route["next_routes"]]), "",
                  "- Próximo objetivo elegido: ____________________",
                  "- Evidencia que respalda la decisión: ____________________",
                  "- Ajustes del recorrido: ____________________", "",
                  "## Procedencia", "",
                  f"Exportación del repositorio lifelong-learning-ecosystem, contrato de datos 1.0, malla {route_id}. Los contenidos fuente corresponden a los archivos canónicos de la copia local utilizada al exportar.", "",
                  "Conservar los registros personales en un espacio privado. El repositorio público contiene diseños curriculares y ejemplos ficticios.", ""])
    return "\n".join(lines)


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--route", required=True, help="Identificador de malla, por ejemplo M-03.")
    parser.add_argument("--output", required=True, type=Path, help="Archivo Markdown de destino.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--force", action="store_true", help="Reemplazar una exportación existente.")
    args = parser.parse_args(argv)
    root, output = args.root.resolve(), args.output.resolve()
    if output.suffix.lower() not in {".md", ".markdown"}:
        print("El destino debe tener extensión .md o .markdown.", file=sys.stderr)
        return 1
    if output in {(root / name).resolve() for name, _ in CANONICAL.values()}:
        print("El destino coincide con un archivo canónico.", file=sys.stderr)
        return 1
    if output.exists() and not args.force:
        print("El archivo ya existe. Elija otra ruta o indique --force para reemplazar la exportación.", file=sys.stderr)
        return 1
    report = validate_repository(root)
    if not report["valid"]:
        print(f"La exportación requiere corregir {len(report['errors'])} error(es). Ejecute python scripts/validate.py.", file=sys.stderr)
        return 1
    try:
        text = render_plan(root, args.route)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
    except (OSError, ValueError) as exc:
        print(f"No se pudo exportar: {exc}", file=sys.stderr)
        return 1
    print(f"Plan exportado: {output}")
    print("Perfil ficticio. Resultados personales sin evaluar.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
