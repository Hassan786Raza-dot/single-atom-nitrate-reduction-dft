#!/usr/bin/env /usr/bin/python3
from pathlib import Path
from ase.build import graphene
from ase.optimize import BFGS
from gpaw import GPAW, PW

out = Path('data/gpaw_smoketest')
out.mkdir(parents=True, exist_ok=True)
atoms = graphene(a=2.46, size=(2, 2, 1), vacuum=12.0)
atoms.calc = GPAW(mode=PW(250), xc='PBE', kpts=(1, 1, 1),
                  occupations={'name': 'fermi-dirac', 'width': 0.1},
                  convergence={'energy': 1e-5}, txt=str(out / 'gpaw.txt'))
energy_before = atoms.get_potential_energy()
opt = BFGS(atoms, logfile=str(out / 'opt.log'))
opt.run(fmax=0.10, steps=25)
energy_after = atoms.get_potential_energy()
atoms.write(out / 'CONTCAR.vasp', format='vasp', direct=True, vasp5=True)
atoms.calc.write(out / 'final.gpw', mode='all')
(out / 'summary.txt').write_text(
    f'energy_before_eV={energy_before:.12f}\n'
    f'energy_after_eV={energy_after:.12f}\n'
    f'converged={opt.converged()}\n', encoding='utf-8')
print((out / 'summary.txt').read_text())
