# Audit Log

## 2026-08-27 — Initial project audit

The project brief was reviewed for scientific, computational, and reproducibility requirements. The requested end-to-end study is larger than can be honestly completed without an installed periodic DFT engine and substantial compute allocation. The workflow was therefore staged: literature and methods are documented, deterministic utilities are tested, and all unexecuted numerical work is labelled as pending.

A methodological inconsistency was identified and corrected in the protocol: molecular ORCA basis-set settings alone are not an adequate specification for periodic 2D-slab calculations requiring Brillouin-zone sampling, work functions, and surface electronic structure. The protocol now separates periodic production calculations from molecular or cluster cross-checks.

A second correction was made to the electrochemical model: CHE is retained as a first-pass framework, but potential dependence of nitrate adsorption and dissociation is explicitly flagged for constant-potential or grand-canonical validation rather than assigned automatically from integer proton/electron counts.

No fabricated DFT energies, barriers, charges, densities of states, or publication claims have been added.

## 2026-08-27 — Test correction

The initial CHE test expected 2.0 eV for `G(H₂)=2.0 eV`, two electron/proton pairs, and `U=-0.5 V`. Applying the documented expression gives 3.0 eV; the test expectation was corrected, then all utility tests and the ten-record literature CSV validation passed.
