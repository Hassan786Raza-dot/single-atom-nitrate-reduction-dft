#!/usr/bin/python3
from __future__ import annotations
import csv
from collections import defaultdict
from pathlib import Path

path = Path('data/convergence/convergence.csv')
with path.open(encoding='utf-8', newline='') as handle:
    rows = list(csv.DictReader(handle))
by_family = defaultdict(list)
for row in rows:
    by_family[row['family']].append(row)

lines = ['# Convergence Analysis', '', '| Family | Cases | Energy range (eV) | Status |', '|---|---:|---:|---|']
for family, family_rows in by_family.items():
    values = [float(r['energy_eV']) for r in family_rows]
    span = max(values) - min(values)
    status = 'PASS' if span < 0.02 else 'REFINE'
    lines.append(f"| {family} | {len(values)} | {span:.6f} | {status} |")
lines += ['', 'The range is a diagnostic for the compact benchmark only. Production convergence must use adsorption and reaction-energy differences for the actual slab family, not isolated total energies alone.']
Path('data/convergence/convergence_analysis.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(lines))
