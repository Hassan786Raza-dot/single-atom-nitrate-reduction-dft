#!/usr/bin/env python3
"""Generate a transparent VASP input package from an ASE-readable structure.

The script deliberately does not create or distribute POTCAR files. A valid
VASP installation must supply POTCARs from the user's licensed library.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from ase.io import read, write


def write_text(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def generate(input_path: str, output_dir: str, system: str, encut: int,
             kmesh: tuple[int, int, int], relax: bool = True) -> Path:
    atoms = read(input_path)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    write(out / "POSCAR", atoms, format="vasp", direct=True, vasp5=True)
    istart = 0
    ibrion = 2 if relax else -1
    nsw = 150 if relax else 0
    incar = f"""SYSTEM = {system}
ENCUT = {encut}
PREC = Accurate
EDIFF = 1E-6
EDIFFG = -0.03
ISMEAR = 0
SIGMA = 0.05
ISPIN = 2
LREAL = Auto
LASPH = .TRUE.
ADDGRID = .TRUE.
ISYM = 0
ISTART = {istart}
IBRION = {ibrion}
NSW = {nsw}
ISIF = 2
LWAVE = .FALSE.
LCHARG = .TRUE.
LDIPOL = .TRUE.
IDIPOL = 3
# Set MAGMOM explicitly per chemical system after spin-state inspection.
# Add a validated solvation model only when supported by the installed VASP build.
"""
    write_text(out / "INCAR", incar)
    write_text(out / "KPOINTS", f"Automatic mesh\n0\nGamma\n{kmesh[0]} {kmesh[1]} {kmesh[2]}\n0 0 0")
    symbols = []
    for atom in atoms:
        if atom.symbol not in symbols:
            symbols.append(atom.symbol)
    write_text(out / "POTCAR.MANIFEST", "\n".join(
        f"{symbol}: provide licensed PAW_PBE potential matching the project pseudopotential policy"
        for symbol in symbols
    ))
    write_text(out / "RUN_NOTES.md", """Before execution, verify the VASP version, PAW/PBE dataset release, ENCUT convergence, k-point convergence, magnetic initialisation, slab vacuum, dipole correction, and charge-compensation policy. Archive OUTCAR, OSZICAR, CONTCAR, vasprun.xml, and the exact input package after the run.""")
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("structure")
    parser.add_argument("output_dir")
    parser.add_argument("--system", default="SAC screening")
    parser.add_argument("--encut", type=int, default=520)
    parser.add_argument("--kmesh", nargs=3, type=int, default=[3, 3, 1])
    parser.add_argument("--single-point", action="store_true")
    args = parser.parse_args()
    generate(args.structure, args.output_dir, args.system, args.encut,
             tuple(args.kmesh), relax=not args.single_point)


if __name__ == "__main__":
    main()
