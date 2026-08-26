#!/usr/bin/python3
from __future__ import annotations
import csv
import re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
md=(root/'manuscript/manuscript.md').read_text(encoding='utf-8')
claims=list(csv.DictReader((root/'claim_evidence_matrix.csv').open(encoding='utf-8', newline='')))
assert len(claims) >= 20
assert all(row['claim_id'].startswith('C') for row in claims)
assert all(row['evidence_path'] and row['allowed_wording'] for row in claims)
assert (root/'figures/final/convergence_benchmark.png').exists()
for p in ['data/convergence/convergence.csv','data/geometry_audit.txt','data/adsorbate_geometry_audit.txt','data/parsed_run_status.csv','limitation_audit.md','production_readiness_checklist.md']:
    assert (root/p).exists(), p
assert 'Table 1' in md and 'Table 2' in md and 'Table 3' in md and 'Table 4' in md and 'Table 5' in md
assert 'Figure 1' in md and 'Equation 1' in md and 'Equation 2' in md and 'Supporting Information' in md
print('repair_claim_rows=',len(claims))
print('REPAIR_PROVENANCE_PASS')
