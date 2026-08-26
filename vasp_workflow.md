# VASP Execution and Audit Protocol

## Licensing and required inputs

VASP is not an open-source executable and requires a valid licence and user-supplied binary. The repository therefore provides input-generation and audit tooling but does not include VASP, `POTCAR` files, or copied proprietary data. The user must provide the executable and PAW potential library before production calculations can begin.

## Baseline input policy

The production method must name the exact VASP version, PAW/PBE potential release, exchange–correlation functional, dispersion implementation, plane-wave cutoff, k-point mesh, smearing, spin initialisation, slab dimensions, vacuum, charge state, dipole correction, and solvation implementation. `ENCUT` must be converged against adsorption-energy differences, not only total energies. The same potential family and numerical policy must be used for every compared system.

For asymmetric slabs and adsorbates, the surface-normal dipole correction must be enabled and aligned with the surface normal. The VASP documentation states that `IDIPOL` selects the correction direction and that `LDIPOL` applies potential and force corrections for charged molecules, slabs, and systems with a net dipole [1] [2]. The exact direction must follow the POSCAR lattice-vector convention rather than being assumed universally.

## Solvation

VASPsol or VASPsol++ may be used only when the compiled VASP build and the solvation code are explicitly recorded. The official VASP resource describes VASPsol as a continuum model for electrostatic screening [3]. Continuum solvation is not a substitute for interfacial validation: shortlisted states should receive explicit-water checks or a constant-potential treatment where feasible.

## Calculation stages

| Stage | Purpose | Required archive |
|---|---|---|
| Support convergence | Cell, slab thickness, vacuum, cutoff, k-points | Inputs, energies, convergence plot, audit record |
| Defect convergence | Defect size and formation energy | POSCAR/INCAR/KPOINTS/OUTCAR and reference states |
| SAC optimisation | Metal anchoring and spin-state comparison | All initial spins, final structures, OUTCAR, CONTCAR |
| Adsorbate screening | Nitrate, H*, OH*, and nitrogen intermediates | Adsorption geometries, energies, charge and spin checks |
| Solvation check | Continuum and explicit-water sensitivity | Solvation parameters and matched state energies |
| Mechanistic refinement | Key PCET steps and transition states | NEB/TS inputs, images, frequencies/connectivity |
| Electrochemical refinement | CHE and selected constant-potential comparison | Potential convention, reference electrode, free-energy ledger |

## Non-negotiable quality gates

A calculation is accepted only if electronic and ionic convergence pass, no unphysical atom contacts remain, the intended magnetic state is stable against alternative initial moments, the slab has adequate vacuum and finite-size control, and the result is linked to a complete raw-output archive. Charged nitrate calculations must document the compensating-background and electrostatic convention. A free-energy diagram must be generated from a machine-readable ledger, not manually transcribed values.

## References

[1]: https://vasp.at/wiki/Electrostatic_corrections "VASP Wiki: Electrostatic corrections"
[2]: https://vasp.at/wiki/LDIPOL "VASP Wiki: LDIPOL"
[3]: https://vasp.at/info/resource/vaspsol/ "VASP: VASPsol resource"
