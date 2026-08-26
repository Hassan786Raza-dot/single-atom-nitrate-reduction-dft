#!/usr/bin/env python3
"""Build a deterministic manifest for the production SAC campaign."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "production_campaign_manifest.csv"

rows: list[dict[str, str]] = []
for structure in sorted((ROOT / "structures" / "initial" / "ase_generated").glob("*/*@*.vasp")):
    name = structure.stem
    support = structure.parent.name
    rows.append({
        "campaign_id": f"bare_{name}",
        "stage": "bare_SAC_optimisation",
        "sac_id": name,
        "adsorbate": "none",
        "support": support,
        "input_structure": str(structure.relative_to(ROOT)),
        "required_checks": "multi_spin;force_convergence;alternative_placement;raw_archive;stability_followup",
        "status": "NOT_RUN",
    })

for structure in sorted((ROOT / "structures" / "initial" / "adsorbates").glob("*/*__*.vasp")):
    name = structure.stem
    sac_id, adsorbate = name.rsplit("__", 1)
    rows.append({
        "campaign_id": f"screen_{name}",
        "stage": "adsorbate_screening",
        "sac_id": sac_id,
        "adsorbate": adsorbate,
        "support": structure.parent.name,
        "input_structure": str(structure.relative_to(ROOT)),
        "required_checks": "charge_convention;dipole_correction;solvation_sensitivity;spin_check;raw_archive",
        "status": "NOT_RUN",
    })

fields = ["campaign_id", "stage", "sac_id", "adsorbate", "support", "input_structure", "required_checks", "status"]
OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print(f"wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
print(f"bare_SAC_optimisation={sum(r['stage']=='bare_SAC_optimisation' for r in rows)}")
print(f"adsorbate_screening={sum(r['stage']=='adsorbate_screening' for r in rows)}")
