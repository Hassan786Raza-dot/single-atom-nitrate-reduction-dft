#!/usr/bin/python3
from __future__ import annotations
from pathlib import Path
import numpy as np
from ase import Atom
from ase.io.vasp import read_vasp
from ase.io import write

ROOT = Path('structures/initial/ase_generated')
OUT = Path('structures/initial/adsorbates')


def metal_position(atoms):
    # The last atom is the isolated metal in the generated SAC structures.
    return atoms.positions[-1].copy()


def nitrate_structure(atoms):
    result = atoms.copy()
    m = metal_position(result)
    result.append(Atom('N', m + np.array([0.0, 0.0, 1.85])))
    result.append(Atom('O', m + np.array([1.15, 0.0, 2.20])))
    result.append(Atom('O', m + np.array([-0.58, 1.00, 2.20])))
    result.append(Atom('O', m + np.array([-0.58, -1.00, 2.20])))
    return result


def hydrogen_structure(atoms):
    result = atoms.copy()
    m = metal_position(result)
    result.append(Atom('H', m + np.array([0.0, 0.0, 1.60])))
    return result


for sac in sorted(ROOT.glob('*/*@*.vasp')):
    with sac.open() as handle:
        atoms = read_vasp(handle)
    relative = sac.relative_to(ROOT)
    target = OUT / relative.parent
    target.mkdir(parents=True, exist_ok=True)
    stem = sac.stem
    write(target / f'{stem}__NO3.vasp', nitrate_structure(atoms), format='vasp', direct=True, vasp5=True)
    write(target / f'{stem}__H.vasp', hydrogen_structure(atoms), format='vasp', direct=True, vasp5=True)
print('generated', len(list(OUT.glob('*/*__*.vasp'))), 'adsorbate structures')
