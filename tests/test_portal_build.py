"""Comprobaciones de privacidad y delimitación del lector HTML autocontenido."""

from pathlib import Path
import json
import runpy
import tempfile
import unittest
from unittest.mock import patch


BUILD = runpy.run_path(str(Path(__file__).resolve().parents[1] / "scripts" / "build_portal.py"))


class PortalBoundaryTests(unittest.TestCase):
    def test_source_fingerprint_normalizes_line_endings(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.toml"
            source.write_bytes(b"[project]\r\nname = 'example'\r\n")
            windows_bytes = BUILD["normalized_source_bytes"](source)
            source.write_bytes(b"[project]\nname = 'example'\n")
            unix_bytes = BUILD["normalized_source_bytes"](source)
            self.assertEqual(windows_bytes, unix_bytes)

    def test_personal_folders_are_not_embedded_as_documents(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ["README.md", "docs/public.md", "private/plan.md", "exports/evidence.md", "docs/private/nested.md"]:
                file = root / name
                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_text("Sentinela para comprobar exclusión.", encoding="utf-8")
            with patch.dict(BUILD["document_paths"].__globals__, {"ROOT": root}):
                observed = {p.relative_to(root).as_posix() for p in BUILD["document_paths"]()}
            self.assertEqual(observed, {"README.md", "docs/public.md"})

    def test_embedded_json_cannot_close_script_element(self):
        original = {"text": '</script><script>alert("texto")</script> & < > \u2028 \u2029'}
        serialized = BUILD["embedded_json"](original)
        self.assertNotIn("</script", serialized.lower())
        self.assertNotIn("<", serialized)
        self.assertNotIn("&", serialized)
        self.assertEqual(json.loads(serialized), original)


if __name__ == "__main__":
    unittest.main()
