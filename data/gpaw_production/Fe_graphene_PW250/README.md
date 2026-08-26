# Fe@graphene_N4 PW250 representative run

This directory contains a representative higher-quality GPAW plane-wave optimisation launched with a 250 eV cut-off, 1×1×1 k-point mesh, a 0.05 eV Å⁻¹ force target, and 40 maximum ionic steps.

The run was interrupted after approximately six ionic steps because the 129-atom periodic calculation consumed the available sandbox CPU and memory for several minutes without reaching the declared force criterion. The partial `gpaw.txt` and `opt.log` files are retained for provenance. No converged final structure, accepted energy, adsorption energy, or catalytic conclusion may be derived from this directory.

Status: `DIAGNOSTIC_ONLY_INTERRUPTED`

The full production campaign must be executed on a suitably resourced workstation or CPU cluster. The machine-readable campaign manifest is `data/production_campaign_manifest.csv`.
