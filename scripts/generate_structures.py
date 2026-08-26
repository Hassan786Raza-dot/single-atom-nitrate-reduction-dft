#!/usr/bin/python3
"""Generate initial periodic support, defect, and bare-SAC geometries.

These are starting structures for optimisation, not relaxed structures or
claims about experimentally preferred anchoring motifs.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from ase import Atom, Atoms
from ase.build import graphene, mx2
from ase.io import write

METALS = ["Fe", "Co", "Ni", "Cu", "Zn", "Ru", "Rh", "Pd", "Pt", "Au"]
SUPPORTS = ["graphene_N4", "MoS2_Svac", "gC3N4_N4"]


def build_gc3n4(size: int = 4, vacuum: float = 18.0) -> Atoms:
    """Build a simple periodic C3N4-like planar model for starting geometries.

    The model is intentionally labelled as a structural starting model; it is
    not a substitute for a literature-validated g-C3N4 polymorph.
    """
    a = 7.13
    atoms = Atoms(cell=[[a * size, 0, 0], [a * size / 2, a * size * 0.8660254, 0], [0, 0, vacuum]], pbc=True)
    basis = [("C", 0.00, 0.00), ("N", 0.50, 0.00), ("C", 0.00, 0.50),
             ("N", 0.50, 0.50), ("C", 0.25, 0.25), ("N", 0.75, 0.25),
             ("N", 0.25, 0.75), ("N", 0.75, 0.75)]
    for i in range(size):
        for j in range(size):
            for symbol, u, v in basis:
                frac = ((i + u) / size, (j + v) / size, 0.5)
                atoms.append(Atom(symbol, atoms.cell.cartesian_positions([frac])[0]))
    return atoms


def build_support(name: str, size: int = 4) -> Atoms:
    if name == "graphene_N4":
        atoms = graphene(a=2.46, size=(size, size, 1), vacuum=18.0)
        # Remove one carbon and replace four nearest carbons by N to define a
        # reproducible defect/anchor family for starting structures.
        del atoms[0]
        dists = atoms.get_distances(0, range(len(atoms)), mic=True)
        nearest = sorted(range(len(atoms)), key=lambda k: dists[k])[:4]
        for index in nearest:
            atoms[index].symbol = "N"
        return atoms
    if name == "MoS2_Svac":
        atoms = mx2("MoS2", kind="2H", a=3.18, thickness=3.13, size=(size, size, 1), vacuum=18.0)
        s_indices = [i for i, atom in enumerate(atoms) if atom.symbol == "S"]
        del atoms[s_indices[0]]
        return atoms
    if name == "gC3N4_N4":
        atoms = build_gc3n4(size=size, vacuum=18.0)
        return atoms
    raise ValueError(f"Unknown support: {name}")


def add_metal(atoms: Atoms, metal: str, support: str) -> Atoms:
    result = atoms.copy()
    # Put the metal near the centre of the cell and 2.0 Å above the mean sheet.
    centre = 0.5 * (result.cell[0] + result.cell[1])
    z = max(result.positions[:, 2]) + 2.0
    if support == "MoS2_Svac":
        z = max(result.positions[:, 2]) + 1.9
    result.append(Atom(metal, position=centre + [0.0, 0.0, z]))
    return result


def generate(output_root: str) -> None:
    root = Path(output_root)
    for support in SUPPORTS:
        pristine = build_support(support)
        support_dir = root / support
        support_dir.mkdir(parents=True, exist_ok=True)
        write(support_dir / "pristine.vasp", pristine, format="vasp", direct=True, vasp5=True)
        write(support_dir / "defect.vasp", pristine, format="vasp", direct=True, vasp5=True)
        for metal in METALS:
            sac = add_metal(pristine, metal, support)
            write(support_dir / f"{metal}@{support}.vasp", sac, format="vasp", direct=True, vasp5=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_root")
    args = parser.parse_args()
    generate(args.output_root)


if __name__ == "__main__":
    main()
