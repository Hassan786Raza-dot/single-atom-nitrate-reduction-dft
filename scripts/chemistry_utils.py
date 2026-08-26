"""Small, dependency-light utilities for reproducible screening bookkeeping.

These functions do not run a quantum-chemistry calculation. They validate and
transform already reported quantities, making assumptions explicit.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

HARTREE_TO_EV = 27.211386245988


def write_orca_input(xyz_text: str, charge: int, multiplicity: int,
                     method: str = "PBE0 D3BJ def2-SVP TightSCF Opt") -> str:
    """Return an ORCA input for a molecular/cluster cross-check."""
    if not xyz_text.strip():
        raise ValueError("xyz_text must contain an XYZ geometry")
    if multiplicity < 1:
        raise ValueError("multiplicity must be a positive integer")
    return f"! {method}\n%pal nprocs 4 end\n* xyz {charge} {multiplicity}\n{xyz_text.rstrip()}\n*\n"


def adsorption_energy(e_complex: float, e_sac: float, e_adsorbate: float) -> float:
    """Compute E_ads in the same energy unit as the inputs."""
    values = (e_complex, e_sac, e_adsorbate)
    if not all(isinstance(v, (int, float)) for v in values):
        raise TypeError("all energies must be numeric")
    return e_complex - e_sac - e_adsorbate


def che_pcet_free_energy(g_h2: float, electrons: int, potential_v: float,
                         proton_corrections: float = 0.0) -> float:
    """Return CHE chemical-potential contribution in eV.

    The convention is n*(0.5*G(H2) - e*U) plus any explicit correction.
    Energies are assumed to be in eV and U in V versus the selected reference.
    """
    if electrons < 0:
        raise ValueError("electrons must be non-negative")
    return electrons * (0.5 * g_h2 - potential_v) + proton_corrections


def read_required_csv(path: str | Path, required: tuple[str, ...]) -> list[dict[str, str]]:
    """Read a CSV and fail loudly when required columns are absent."""
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fields = tuple(reader.fieldnames or ())
        missing = [name for name in required if name not in fields]
        if missing:
            raise ValueError(f"{path}: missing columns: {', '.join(missing)}")
        return list(reader)


@dataclass(frozen=True)
class ReactionStep:
    name: str
    delta_g_ev: float
    proton_electron_pairs: int = 0


def limiting_potential(steps: list[ReactionStep], target_potential: float = 0.0) -> float:
    """Return the CHE limiting potential for uphill steps.

    For a step with n proton/electron pairs, the potential required to make the
    step non-uphill is deltaG/n. Non-PCET steps are excluded from this metric.
    """
    candidates = [s.delta_g_ev / s.proton_electron_pairs for s in steps
                  if s.proton_electron_pairs > 0]
    if not candidates:
        raise ValueError("at least one PCET step is required")
    return target_potential - max(candidates)
