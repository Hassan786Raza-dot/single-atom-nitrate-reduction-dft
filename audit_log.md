# Audit Log

## 2026-08-27 — Initial project audit

The project brief was reviewed for scientific, computational, and reproducibility requirements. The requested end-to-end study is larger than can be honestly completed without an installed periodic DFT engine and substantial compute allocation. The workflow was therefore staged: literature and methods are documented, deterministic utilities are tested, and all unexecuted numerical work is labelled as pending.

A methodological inconsistency was identified and corrected in the protocol: molecular ORCA basis-set settings alone are not an adequate specification for periodic 2D-slab calculations requiring Brillouin-zone sampling, work functions, and surface electronic structure. The protocol now separates periodic production calculations from molecular or cluster cross-checks.

A second correction was made to the electrochemical model: CHE is retained as a first-pass framework, but potential dependence of nitrate adsorption and dissociation is explicitly flagged for constant-potential or grand-canonical validation rather than assigned automatically from integer proton/electron counts.

No fabricated DFT energies, barriers, charges, densities of states, or publication claims have been added.

## 2026-08-27 — Test correction

The initial CHE test expected 2.0 eV for `G(H₂)=2.0 eV`, two electron/proton pairs, and `U=-0.5 V`. Applying the documented expression gives 3.0 eV; the test expectation was corrected, then all utility tests and the ten-record literature CSV validation passed.

## 2026-08-27 — Open-source periodic-DFT route and geometry generation

VASP, Quantum ESPRESSO, CP2K, ORCA, and xTB were unavailable in the initial environment. VASP cannot be installed without a valid licence and executable. Ubuntu's open-source GPAW package was installed after resolving compiler, LibXC, Python-header, and NumPy/SciPy ABI dependencies in an isolated `.venv-gpaw` environment. A periodic GPAW smoke test completed successfully.

The ASE structure generator initially failed because of version-specific builder arguments and an incorrectly scaled g-C3N4 fractional-coordinate construction. Both defects were corrected. The regenerated structure set contains 36 files: three pristine/defect support models and 30 bare SAC starting geometries. The automated geometry audit now reports zero failures.

A first genuine Fe@graphene periodic GPAW optimisation converged in 12 ionic steps under a low-cost LCAO pre-screening setting. This is a computational smoke/pre-screen result, not yet a publication-grade convergence result.
