"""Pruebas de riesgos concretos: integridad, ciclos, rutas, enlaces y exportación.

Ejecutar desde la raíz: python -m unittest discover -s tests -v
Los datos mínimos son ficticios y se crean en directorios temporales.
"""

from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from validate import LEVELS, validate_repository  # noqa: E402
from export_plan import render_plan  # noqa: E402


def write_json(root, relative, value):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def fixture(root):
    for relative, text in {
        "README.md": '# Ecosistema\n\n[Inicio](docs/support.md#cómo-comenzar)\n\n[Guía](<docs/Guía con espacios.md#paso-inicial>)\n\n[Consultar][guia]\n\n[guia]: docs/Guía%20con%20espacios.md#paso-inicial "Guía"\n',
        "docs/program.md": "# Integración\n\nPropuesta ficticia.\n",
        "docs/support.md": "# Apoyo\n\n## Cómo comenzar\n\nTexto.\n\n## Cómo comenzar\n\nOtro apartado.\n",
        "docs/rubric.md": "# Rúbrica\n\nRevisión pendiente.\n",
        "docs/route.md": "# Malla\n\nDiseño ficticio.\n",
        "docs/Guía con espacios.md": "# Guía\n\n## Paso inicial\n\nConsultar recursos.\n",
        "portal/index.html": '<!doctype html><html lang="es"><head><link rel="stylesheet" href="assets/app.css"></head><body><h1 id="panel">Panel</h1><a href="#panel">Volver</a><a href="../README.md#ecosistema">README</a><script src="assets/app.js"></script></body></html>',
        "portal/assets/app.css": "body { color: black; }\n",
        "portal/assets/app.js": '"use strict";\n',
    }.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    program = {"id": "PRG-ONE", "name": "Programa de prueba", "repository": "example/program",
               "url": "https://example.org/program", "description": "Ejemplo para pruebas locales.",
               "role": "programa", "domains": ["Ejemplo"], "audiences": ["Persona adulta"],
               "review": {"status": "readme_revisado", "reviewed_on": "2026-10-05", "source_url": "https://example.org/program/README.md",
                          "content_sha": "abc123", "scope": "Sólo README.", "declared_content_status": "Propuesta editorial.", "human_validation": False},
               "entry_points": [{"label": "README", "url": "https://example.org/program/README.md", "verification": "recurso_leido"}],
               "competency_ids": ["C-ONE"], "license_note": "Revisar la licencia de origen.", "integration_doc": "docs/program.md"}
    competency = {"id": "C-ONE", "title": "Formular un objetivo", "domain": "Aprendizaje", "description": "Definir un resultado verificable.",
                  "prerequisites": [], "outcomes": ["Formula un objetivo."], "evidence": ["Objetivo escrito."], "program_ids": ["PRG-ONE"],
                  "transfer_task": "Aplicar a otro tema.", "review_status": "propuesta_editorial",
                  "level_descriptors": {level: f"Descriptor observable de {level}." for level in LEVELS}}
    other = copy.deepcopy(competency)
    other.update({"id": "C-TWO", "title": "Planificar", "prerequisites": ["C-ONE"]})
    support = {"id": "SUP-ONE", "title": "Apoyo de estudio", "purpose": "Preparar el entorno.", "trigger": "La persona requiere orientación.",
               "activities": ["Elegir un lugar."], "success_criteria": ["Explica su elección."], "program_ids": ["PRG-ONE"],
               "competency_ids": ["C-ONE"], "doc_path": "docs/support.md", "status": "guia_inicial"}
    rubric = {"id": "RUB-ONE", "title": "Evidencias", "purpose": "Revisar el aprendizaje.",
              "criteria": [{"id": "CR-ONE", "title": "Claridad", "descriptors": {str(value): f"Descriptor observable {value}." for value in range(4)}}],
              "decision_rule": "Decisión razonada por criterio.", "limitations": "No es una prueba validada.", "doc_path": "docs/rubric.md"}
    step = {"id": "STEP-1", "title": "Comenzar", "outcomes": ["Explica el objetivo."], "competency_ids": ["C-ONE"],
            "program_ids": ["PRG-ONE"], "support_ids": ["SUP-ONE"], "requires": [], "activities": ["Escribir un objetivo."],
            "evidence": ["Texto inicial."], "acceptance_criteria": ["El resultado puede observarse."],
            "alternatives": ["Dictar el objetivo."], "availability": "Actividad original incluida; alineación externa pendiente."}
    step_two = copy.deepcopy(step)
    step_two.update({"id": "STEP-2", "title": "Revisar", "requires": ["STEP-1"]})
    route = {"id": "M-03", "title": "Reconversión", "purpose": "Definir una nueva trayectoria.", "audience": ["Personas adultas"],
             "life_contexts": ["reconversion"], "entry_profile": "Revisar conocimientos previos.", "entry_competencies": [],
             "competency_ids": ["C-ONE", "C-TWO"], "program_ids": ["PRG-ONE"], "support_ids": ["SUP-ONE"],
             "diagnostic": ["Explicar la experiencia previa."], "objectives": ["Construye un plan."], "steps": [step, step_two],
             "assessment": {"rubric_id": "RUB-ONE", "evidence": ["Plan."], "criteria": ["Coherencia."]},
             "next_routes": ["M-05"], "status": "diseno_inicial", "content_readiness": "Diseño y actividades iniciales.", "doc_path": "docs/route.md"}
    second_route = copy.deepcopy(route)
    second_route.update({"id": "M-05", "title": "Interés personal", "next_routes": ["M-03"]})
    second_route["steps"][0]["id"] = "OTHER-1"
    second_route["steps"][1].update({"id": "OTHER-2", "requires": ["OTHER-1"]})
    data = {
        "catalog/programs.json": {"schema_version": "1.0", "reviewed_on": "2026-10-05", "scope_note": "Datos ficticios.", "programs": [program]},
        "catalog/pending.json": {"schema_version": "1.0", "items": []},
        "competencies/competencies.json": {"schema_version": "1.0", "levels": LEVELS, "competencies": [competency, other]},
        "support/resources.json": {"schema_version": "1.0", "resources": [support]},
        "assessment/rubrics.json": {"schema_version": "1.0", "scale": [{"value": value, "label": f"Nivel {value}"} for value in range(4)], "rubrics": [rubric]},
        "curricula/mallas.json": {"schema_version": "1.0", "curricula": [route, second_route]},
    }
    for filename, value in data.items():
        write_json(root, filename, value)
    return data


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = fixture(self.root)

    def rewrite(self, filename):
        write_json(self.root, filename, self.data[filename])

    def router_html(self, links):
        target = self.root / "portal/index.html"
        html = target.read_text(encoding="utf-8")
        meta = '<meta name="lle-router" content="hash"><meta name="lle-routes" content="inicio mallas programas competencias apoyos evaluacion documentos"><meta name="lle-document-root" content="..">'
        html = html.replace("<head>", "<head>" + meta)
        html = html.replace("</body>", "".join(f'<a href="{link}">Ruta</a>' for link in links) + "</body>")
        target.write_text(html, encoding="utf-8")
        return target

    def assert_code(self, code):
        report = validate_repository(self.root)
        self.assertFalse(report["valid"])
        self.assertIn(code, {error["code"] for error in report["errors"]}, report)
        return report

    def test_valid_fixture_and_next_route_cycle_allowed(self):
        report = validate_repository(self.root)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(report["counts"]["curricula"], 2)
        self.assertFalse(report["network_used"])

    def test_unknown_reference_to_each_entity(self):
        filename = "curricula/mallas.json"
        for field in ("program_ids", "competency_ids", "support_ids", "entry_competencies", "next_routes"):
            with self.subTest(field=field):
                original = copy.deepcopy(self.data[filename])
                self.data[filename]["curricula"][0][field] = ["UNKNOWN-ID"]
                self.rewrite(filename)
                self.assert_code("REF_UNKNOWN")
                self.data[filename] = original
                self.rewrite(filename)

    def test_unknown_assessment_rubric(self):
        self.data["curricula/mallas.json"]["curricula"][0]["assessment"]["rubric_id"] = "RUB-MISSING"
        self.rewrite("curricula/mallas.json")
        self.assert_code("REF_UNKNOWN")

    def test_duplicate_global_id(self):
        self.data["support/resources.json"]["resources"][0]["id"] = "PRG-ONE"
        self.rewrite("support/resources.json")
        self.assert_code("ID_DUPLICATE")

    def test_competency_prerequisite_cycle(self):
        self.data["competencies/competencies.json"]["competencies"][0]["prerequisites"] = ["C-TWO"]
        self.rewrite("competencies/competencies.json")
        self.assert_code("GRAPH_CYCLE")

    def test_step_prerequisite_cycle(self):
        self.data["curricula/mallas.json"]["curricula"][0]["steps"][0]["requires"] = ["STEP-2"]
        self.rewrite("curricula/mallas.json")
        self.assert_code("GRAPH_CYCLE")

    def test_step_from_another_route_is_rejected(self):
        self.data["curricula/mallas.json"]["curricula"][0]["steps"][0]["requires"] = ["OTHER-1"]
        self.rewrite("curricula/mallas.json")
        self.assert_code("STEP_REF_UNKNOWN")

    def test_document_path_traversal_and_absolute_paths(self):
        filename = "support/resources.json"
        for path in ("../outside.md", "%2e%2e/outside.md", "/tmp/example.md", "C:\\private\\example.md"):
            with self.subTest(path=path):
                self.data[filename]["resources"][0]["doc_path"] = path
                self.rewrite(filename)
                self.assert_code("PATH_UNSAFE")

    def test_missing_document(self):
        (self.root / "docs/program.md").unlink()
        self.assert_code("PATH_MISSING")

    def test_invalid_json_and_duplicate_json_keys(self):
        target = self.root / "catalog/pending.json"
        for text in ('{"schema_version":', '{"schema_version":"1.0","schema_version":"2.0","items":[]}', '{"schema_version":"1.0","items":NaN}'):
            with self.subTest(text=text):
                target.write_text(text, encoding="utf-8")
                self.assert_code("JSON_PARSE")

    def test_nonobject_json_root(self):
        (self.root / "catalog/pending.json").write_text("[]", encoding="utf-8")
        self.assert_code("JSON_TYPE")

    def test_invalid_field_type_does_not_crash(self):
        self.data["competencies/competencies.json"]["competencies"][0]["prerequisites"] = {"bad": "shape"}
        self.data["curricula/mallas.json"]["curricula"][0]["steps"][0]["id"] = {"unexpected": "object"}
        self.rewrite("competencies/competencies.json")
        self.rewrite("curricula/mallas.json")
        self.assert_code("FIELD_TYPE")

    def test_missing_level_descriptor(self):
        del self.data["competencies/competencies.json"]["competencies"][0]["level_descriptors"][LEVELS[-1]]
        self.rewrite("competencies/competencies.json")
        self.assert_code("LEVEL_DESCRIPTORS")

    def test_undeclared_state(self):
        self.data["curricula/mallas.json"]["curricula"][0]["status"] = "certificado"
        self.rewrite("curricula/mallas.json")
        self.assert_code("STATE_INVALID")

    def test_boolean_is_not_a_rubric_scale_integer(self):
        self.data["assessment/rubrics.json"]["scale"][0]["value"] = False
        self.rewrite("assessment/rubrics.json")
        self.assert_code("SCALE_INVALID")

    def test_invalid_rubric_descriptors(self):
        del self.data["assessment/rubrics.json"]["rubrics"][0]["criteria"][0]["descriptors"]["3"]
        self.rewrite("assessment/rubrics.json")
        self.assert_code("RUBRIC_DESCRIPTORS")

    def test_url_syntax(self):
        self.data["catalog/programs.json"]["programs"][0]["url"] = "https://bad host/"
        self.rewrite("catalog/programs.json")
        self.assert_code("URL_INVALID")

    def test_markdown_fragments_spaces_accents_and_duplicates(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write('\n[Segunda sección](docs/support.md#cómo-comenzar-1)\n\n[Con espacios](docs/Guía con espacios.md#paso-inicial)\n')
        report = validate_repository(self.root)
        self.assertTrue(report["valid"], report["errors"])

    def test_nonexistent_fragment(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Destino](docs/support.md#fragmento-inexistente)\n")
        self.assert_code("LINK_FRAGMENT")

    def test_markdown_code_examples_are_not_links(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write('\n```markdown\n[Ejemplo](archivo-ficticio.md)\n```\n\n`[Inline](tampoco-existe.md)`\n')
        report = validate_repository(self.root)
        self.assertTrue(report["valid"], report["errors"])

    def test_link_traversal(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Fuera](../private.md)\n")
        self.assert_code("LINK_UNSAFE")

    def test_missing_html_asset(self):
        (self.root / "portal/assets/app.js").unlink()
        self.assert_code("LINK_MISSING")

    def test_declared_router_routes_entities_documents_and_normal_anchor(self):
        self.router_html(["#inicio", "#mallas", "#programas", "#competencias", "#apoyos", "#evaluacion", "#documentos",
                          "#malla/M-03", "#programa/PRG-ONE", "#competencia/C-ONE", "#apoyo/SUP-ONE", "#rubrica/RUB-ONE",
                          "#doc/docs%2Fsupport.md?a=como-comenzar-1", "#doc/docs%2FGu%C3%ADa%20con%20espacios.md?a=paso-inicial", "#panel"])
        report = validate_repository(self.root)
        self.assertTrue(report["valid"], report["errors"])

    def test_router_does_not_ignore_unknown_normal_anchors(self):
        self.router_html(["#main-content-absent", "#seccion-inventada"])
        self.assert_code("LINK_FRAGMENT")

    def test_router_rejects_unknown_entity_id(self):
        self.router_html(["#malla/M-404"])
        self.assert_code("ROUTER_REF_UNKNOWN")

    def test_router_rejects_missing_document(self):
        self.router_html(["#doc/docs%2Fmissing.md"])
        self.assert_code("ROUTER_DOC_MISSING")

    def test_router_rejects_document_traversal(self):
        self.router_html(["#doc/%2E%2E%2Foutside.md"])
        self.assert_code("ROUTER_PATH")

    def test_router_rejects_missing_document_heading(self):
        self.router_html(["#doc/docs%2Fsupport.md?a=encabezado-inexistente"])
        self.assert_code("ROUTER_DOC_FRAGMENT")

    def test_router_rejects_undeclared_sections_and_wrong_document_root(self):
        target = self.router_html(["#inicio"])
        valid = target.read_text(encoding="utf-8")
        for invalid in (valid.replace("inicio mallas programas", "inventada mallas programas"),
                        valid.replace('content=".."', 'content="../.."')):
            with self.subTest(case=invalid):
                target.write_text(invalid, encoding="utf-8")
                self.assert_code("ROUTER_DECLARATION")

    def test_missing_markdown_reference_definition(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Documento][definicion-ausente]\n")
        self.assert_code("LINK_REFERENCE")

    def test_read_only_and_no_network(self):
        before = {str(path.relative_to(self.root)): path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        with patch.object(socket, "create_connection", side_effect=AssertionError("Red prohibida en validación")):
            report = validate_repository(self.root)
        after = {str(path.relative_to(self.root)): path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(before, after)
        self.assertNotIn(str(self.root), json.dumps(report))

    def test_private_and_exported_documents_are_not_inspected(self):
        for folder in ("private", "exports"):
            target = self.root / folder / "plan-personal.md"
            target.parent.mkdir()
            target.write_text("# Privado\n\n[Evidencia personal](../archivo-no-distribuido.pdf)\n", encoding="utf-8")
        report = validate_repository(self.root)
        self.assertTrue(report["valid"], report["errors"])

    def test_cli_json_and_report(self):
        destination = self.root / "report.json"
        result = subprocess.run([sys.executable, str(SCRIPTS / "validate.py"), "--root", str(self.root), "--json", "--report", str(destination)], capture_output=True, text=True, encoding="utf-8", check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)["valid"])
        self.assertEqual(json.loads(result.stdout), json.loads(destination.read_text(encoding="utf-8")))

    def test_cli_failing_exit_code(self):
        (self.root / "catalog/pending.json").unlink()
        result = subprocess.run([sys.executable, str(SCRIPTS / "validate.py"), "--root", str(self.root), "--json"], capture_output=True, text=True, encoding="utf-8", check=False)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertFalse(json.loads(result.stdout)["valid"])

    def test_cli_utf8_when_shell_default_is_ascii(self):
        result = subprocess.run([sys.executable, str(SCRIPTS / "validate.py"), "--root", str(self.root), "--json"], capture_output=True, text=True, encoding="utf-8", env=dict(os.environ, PYTHONIOENCODING="ascii"), check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)["valid"])

    def test_export_never_assigns_mastery(self):
        text = render_plan(self.root, "M-03")
        self.assertIn("Estado personal inicial:** sin evaluar", text)
        self.assertIn("Resultado personal:** sin evaluar", text)
        self.assertIn("Perfil:** ejemplo ficticio sin datos personales", text)
        self.assertIn("STEP-2", text)
        self.assertIn("https://example.org/program", text)
        self.assertIn("Descriptor observable 3", text)

    def test_export_cli_and_unknown_route(self):
        output = self.root / "plan.md"
        result = subprocess.run([sys.executable, str(SCRIPTS / "export_plan.py"), "--root", str(self.root), "--route", "M-03", "--output", str(output)], capture_output=True, text=True, encoding="utf-8", check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(output.is_file())
        with self.assertRaises(ValueError):
            render_plan(self.root, "M-404")


if __name__ == "__main__":
    unittest.main()
