#!/usr/bin/env /usr/bin/python3
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
from ase.io.vasp import read_vasp


def audit(path: Path) -> list[str]:
    with path.open('r', encoding='utf-8') as handle:
        atoms = read_vasp(handle)
    errors = []
    lengths = atoms.cell.lengths()
    if not np.all(np.isfinite(lengths)) or min(lengths) <= 0:
        errors.append('invalid cell')
    if not all(atoms.pbc):
        errors.append('non-periodic cell')
    zspan = np.ptp(atoms.positions[:, 2]) if len(atoms) else 0.0
    if lengths[2] - zspan < 15.0:
        errors.append(f'vacuum below 15 A: {lengths[2]-zspan:.3f}')
    if len(atoms) > 1:
        d = atoms.get_all_distances(mic=True)
        d += np.eye(len(atoms)) * 1e6
        if np.min(d) < 0.7:
            errors.append(f'atom contact below 0.7 A: {np.min(d):.3f}')
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('root')
    args = parser.parse_args()
    files = sorted(Path(args.root).rglob('*.vasp'))
    failures = 0
    for path in files:
        errors = audit(path)
        if errors:
            failures += 1
            print(f'FAIL {path}: {"; ".join(errors)}')
        else:
            print(f'PASS {path}')
    print(f'checked={len(files)} failures={failures}')
    raise SystemExit(1 if failures else 0)


if __name__ == '__main__':
    main()
