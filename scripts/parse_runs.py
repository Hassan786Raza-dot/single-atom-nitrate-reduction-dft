#!/usr/bin/python3
from __future__ import annotations
import csv
import re
from pathlib import Path

ROOTS = [Path('data/gpaw_runs'), Path('data/gpaw_smoketest')]
rows = []
for root in ROOTS:
    if not root.exists():
        continue
    for summary in sorted(root.glob('*/summary.txt')):
        values = {}
        for line in summary.read_text(encoding='utf-8').splitlines():
            if '=' in line:
                key, value = line.split('=', 1)
                values[key] = value
        rows.append({
            'run_dir': str(summary.parent),
            'structure': values.get('structure', 'smoke-test'),
            'energy_before_eV': values.get('energy_before_eV', 'NR'),
            'energy_after_eV': values.get('energy_after_eV', 'NR'),
            'converged': values.get('converged', 'NR'),
            'optimizer_steps': values.get('optimizer_steps', 'NR'),
            'acceptance': 'PASS' if values.get('converged') == 'True' else 'DIAGNOSTIC_ONLY',
        })

out = Path('data/parsed_run_status.csv')
with out.open('w', newline='', encoding='utf-8') as handle:
    fields = list(rows[0]) if rows else ['run_dir']
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
print(f'parsed_runs={len(rows)} output={out}')
