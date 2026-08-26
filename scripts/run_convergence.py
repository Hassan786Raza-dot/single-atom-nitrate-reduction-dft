#!/usr/bin/python3
from __future__ import annotations
import csv
from pathlib import Path
from ase.build import graphene
from gpaw import GPAW, PW

OUT = Path('data/convergence')
OUT.mkdir(parents=True, exist_ok=True)
rows = []

cases = []
for cutoff in (150, 250, 350):
    cases.append(('cutoff', str(cutoff), cutoff, (1, 1, 1), 12.0, False))
for kmesh in ((1, 1, 1), (2, 2, 1), (3, 3, 1)):
    cases.append(('kmesh', 'x'.join(map(str, kmesh)), 250, kmesh, 12.0, False))
for vacuum in (10.0, 15.0, 20.0):
    cases.append(('vacuum', str(vacuum), 250, (1, 1, 1), vacuum, False))
for spinpol in (False, True):
    cases.append(('spin', str(spinpol), 250, (1, 1, 1), 15.0, spinpol))

for family, label, cutoff, kmesh, vacuum, spinpol in cases:
    name = f'{family}_{label}'.replace('.', 'p')
    path = OUT / name
    path.mkdir(exist_ok=True)
    atoms = graphene(a=2.46, size=(2, 2, 1), vacuum=vacuum)
    atoms.calc = GPAW(mode=PW(cutoff), xc='PBE', kpts=kmesh,
                      spinpol=spinpol,
                      occupations={'name': 'fermi-dirac', 'width': 0.1},
                      convergence={'energy': 1e-5}, txt=str(path / 'gpaw.txt'))
    energy = atoms.get_potential_energy()
    atoms.calc.write(path / 'result.gpw', mode='all')
    rows.append({'family': family, 'label': label, 'cutoff_eV': cutoff,
                 'kmesh': 'x'.join(map(str, kmesh)), 'vacuum_A': vacuum,
                 'spinpol': spinpol, 'energy_eV': f'{energy:.12f}'})

with (OUT / 'convergence.csv').open('w', newline='', encoding='utf-8') as handle:
    writer = csv.DictWriter(handle, fieldnames=rows[0])
    writer.writeheader()
    writer.writerows(rows)
print(f'completed={len(rows)}')
