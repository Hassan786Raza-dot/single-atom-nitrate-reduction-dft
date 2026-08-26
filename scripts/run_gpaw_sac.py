#!/usr/bin/env /usr/bin/python3
from __future__ import annotations
import argparse
from pathlib import Path
from ase.io.vasp import read_vasp
from ase.optimize import BFGS
from gpaw import GPAW, PW


def run(structure: str, output: str, fmax: float, steps: int, kmesh: tuple[int,int,int], basis: str, cutoff: float) -> None:
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    with Path(structure).open('r', encoding='utf-8') as handle:
        atoms = read_vasp(handle)
    atoms.calc = GPAW(mode=PW(cutoff), xc='PBE', kpts=kmesh,
                      occupations={'name': 'fermi-dirac', 'width': 0.1},
                      convergence={'energy': 1e-5}, txt=str(out / 'gpaw.txt'))
    energy_before = atoms.get_potential_energy()
    optimiser = BFGS(atoms, logfile=str(out / 'opt.log'))
    optimiser.run(fmax=fmax, steps=steps)
    energy_after = atoms.get_potential_energy()
    atoms.write(out / 'CONTCAR.vasp', format='vasp', direct=True, vasp5=True)
    atoms.calc.write(out / 'final.gpw', mode='all')
    (out / 'summary.txt').write_text(
        f'structure={structure}\nenergy_before_eV={energy_before:.12f}\n'
        f'energy_after_eV={energy_after:.12f}\nconverged={optimiser.converged()}\n'
        f'optimizer_steps={optimiser.nsteps}\n', encoding='utf-8')
    print((out / 'summary.txt').read_text())


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument('structure')
    p.add_argument('output')
    p.add_argument('--fmax', type=float, default=0.10)
    p.add_argument('--steps', type=int, default=40)
    p.add_argument('--kmesh', nargs=3, type=int, default=[1, 1, 1])
    p.add_argument('--basis', default='unused')
    p.add_argument('--cutoff', type=float, default=250.0)
    args = p.parse_args()
    run(args.structure, args.output, args.fmax, args.steps, tuple(args.kmesh), args.basis, args.cutoff)


if __name__ == '__main__':
    main()
