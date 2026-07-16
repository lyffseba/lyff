#!/usr/bin/env python3
"""Offline unit tests for the lyff hub CLI (no network)."""
from __future__ import annotations

import importlib.util
import subprocess
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "bin" / "lyff"


def load_lyff():
    # bin/lyff has no .py suffix
    from importlib.machinery import SourceFileLoader
    from importlib.util import module_from_spec, spec_from_loader

    loader = SourceFileLoader("lyff_cli", str(CLI))
    spec = spec_from_loader(loader.name, loader)
    assert spec is not None
    mod = module_from_spec(spec)
    loader.exec_module(mod)
    return mod


class TestRegistry(unittest.TestCase):
    def setUp(self):
        self.lyff = load_lyff()
        self.reg = self.lyff.load_registry()

    def test_projects_present(self):
        ids = {p["id"] for p in self.reg["projects"]}
        for need in ("43", "44", "ai", "bet", "ents", "maxi", "rugs", "witness"):
            self.assertIn(need, ids)

    def test_ids_are_strings(self):
        for p in self.reg["projects"]:
            self.assertIsInstance(p["id"], str)
            self.assertIsInstance(p["path"], str)

    def test_validate_schema(self):
        errs = self.lyff.validate_registry(self.reg, check_paths=False)
        self.assertEqual(errs, [], msg=errs)

    def test_validate_full_when_workspace_present(self):
        # Full path checks only when nested projects exist (local workspace).
        if not (ROOT / "bet" / ".git").exists():
            self.skipTest("nested workspace not present")
        errs = self.lyff.validate_registry(self.reg, check_paths=True)
        self.assertEqual(errs, [], msg=errs)

    def test_project_by_id(self):
        p = self.lyff.project_by_id(self.reg, "bet")
        self.assertIsNotNone(p)
        self.assertEqual(p["id"], "bet")
        self.assertTrue(self.lyff.project_path(p).is_dir())

    def test_unknown_project(self):
        self.assertIsNone(self.lyff.project_by_id(self.reg, "nope"))


class TestCLISubprocess(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(CLI), *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

    def test_version(self):
        r = self.run_cli("version")
        self.assertEqual(r.returncode, 0)
        self.assertRegex(r.stdout.strip(), r"^\d+\.\d+\.\d+$")

    def test_help(self):
        r = self.run_cli("help")
        self.assertEqual(r.returncode, 0)
        self.assertIn("status", r.stdout)

    def test_list(self):
        r = self.run_cli("list")
        self.assertEqual(r.returncode, 0)
        self.assertIn("bet", r.stdout)

    def test_status(self):
        r = self.run_cli("status")
        self.assertEqual(r.returncode, 0)
        self.assertIn("lyff hub", r.stdout)
        self.assertIn("43", r.stdout)

    def test_validate(self):
        r = self.run_cli("validate", "--schema")
        self.assertEqual(r.returncode, 0)
        self.assertIn("registry ok", r.stdout)

    def test_path_bet(self):
        if not (ROOT / "bet").is_dir():
            self.skipTest("nested workspace not present")
        r = self.run_cli("path", "bet")
        self.assertEqual(r.returncode, 0)
        self.assertTrue(Path(r.stdout.strip()).is_dir())

    def test_docs_index(self):
        r = self.run_cli("docs", "index")
        self.assertEqual(r.returncode, 0)
        self.assertIn("lyff documentation", r.stdout)

    def test_unknown_command(self):
        r = self.run_cli("not-a-command")
        self.assertNotEqual(r.returncode, 0)


class TestBundle(unittest.TestCase):
    def test_bundle_creates_archive(self):
        lyff = load_lyff()
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "test.tgz"
            rc = lyff.cmd_bundle(str(out))
            self.assertEqual(rc, 0)
            self.assertTrue(out.is_file())
            self.assertGreater(out.stat().st_size, 1000)
            with tarfile.open(out, "r:gz") as tar:
                names = tar.getnames()
            self.assertTrue(any(n.endswith("bin/lyff") for n in names))
            self.assertTrue(any(n.endswith("registry.yaml") for n in names))
            # heavy dirs excluded
            self.assertFalse(any("/node_modules/" in n for n in names))
            self.assertFalse(any("/.pixi/" in n for n in names))
            self.assertFalse(any("/.venv/" in n for n in names))


if __name__ == "__main__":
    unittest.main()
