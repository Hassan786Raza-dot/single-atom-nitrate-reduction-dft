#!/usr/bin/env python3
"""Run the repository validation suite with explicit, reproducible commands."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run(label: str, command: list[str]) -> None:
    print(f"=== {label} ===")
    print("$ " + " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    run("chemistry utility tests", [PYTHON, "scripts/tests/test_chemistry_utils.py"])
    run("VASP input-generator tests", [PYTHON, "scripts/tests/test_vasp_inputs.py"])
    run("geometry audit", [PYTHON, "scripts/audit_geometries.py", "structures/initial"])
    run("curated-reference audit", [PYTHON, "scripts/validate_curated_refs.py"])
    run("repair-provenance audit", [PYTHON, "scripts/validate_repairs.py"])
    run("citation and cross-reference audit", [PYTHON, "scripts/audit_citations_crossrefs.py"])
    run("final project audit", [PYTHON, "scripts/final_audit.py"])
    print("VALIDATION_SUITE_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
