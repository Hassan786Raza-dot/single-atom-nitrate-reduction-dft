# Production campaign protocol

This protocol is the executable continuation of the reproducibility benchmark. It is designed for a licensed VASP installation or a suitably resourced GPAW workstation/cluster. It does not convert unexecuted templates into results.

## Stage 0: environment registration

Record the hostname, CPU count, memory, operating system, Python version, GPAW or VASP version, exchange-correlation functional, PAW dataset release, dispersion implementation, solvation implementation, MPI/OpenMP settings, and the complete environment lock. For VASP, record the licence holder and executable version without distributing proprietary binaries or potentials.

## Stage 1: support and defect convergence

For each support family, converge the in-plane cell, slab size, vacuum height, plane-wave cut-off, k-point mesh, smearing, dipole correction, and force threshold. Repeat the tests for representative defect structures. Use adsorption-energy differences, forces, relaxed geometry, magnetic moments, and relevant work-function changes as observables. Absolute total-energy ranges are diagnostic only.

Archive every input, output, final geometry, convergence table, plot source, and audit result under a unique calculation identifier.

## Stage 2: bare-SAC optimisation

Run every row with `stage=bare_SAC_optimisation` in `data/production_campaign_manifest.csv`. For every metal/support pair, use the converged settings and multiple initial magnetic moments. Where chemically plausible, include alternative metal placements and coordination motifs. Retain all converged and failed attempts, select the lowest valid state only after checking magnetic and structural alternatives, and never delete metastable or reconstructed outcomes.

Accept a structure only when electronic convergence, ionic force convergence, contact checks, geometry checks, and raw-output completeness all pass. Add migration, aggregation, reconstruction, dissolution, and defect-formation follow-ups before describing a site as stable.

Example GPAW command:

```bash
.venv-gpaw/bin/python scripts/run_gpaw_sac.py \
  structures/initial/ase_generated/graphene_N4/Fe@graphene_N4.vasp \
  data/gpaw_production/Fe_graphene_PW350 \
  --cutoff 350 --kmesh 3 3 1 --fmax 0.03 --steps 200
```

This command is an execution template. Its output must pass the acceptance rules before entering any chemical dataset.

## Stage 3: nitrate and H* screening

Run every nitrate and H* row only after its corresponding bare SAC is accepted. Declare the nitrate charge, compensating background, electrostatic correction, dipole treatment, reference state, solvation model, and potential convention before execution. Use identical numerical and thermodynamic conventions for each compared state.

For each accepted complex, archive initial and final structures, charge and spin information, adsorption-energy components, solvation settings, convergence records, and geometry audits. A starting nitrate geometry is not an adsorption result.

## Stage 4: complete reaction network

For shortlisted sites, calculate nitrate-to-nitrite, nitrite-to-ammonia, hydrogenation, oxygen-removal, ammonia-release, and HER alternatives. Apply CHE only to appropriate proton–electron-transfer steps. Use potential-dependent or grand-canonical checks for charge-sensitive states. Add thermochemical corrections using a documented vibrational or approximation protocol.

Transition states require a converged saddle-point calculation, one relevant imaginary mode, and connectivity checks to the intended reactant and product. Generate every free-energy diagram from a machine-readable ledger.

## Stage 5: solvation, stability, and uncertainty

Repeat ranking-critical states with the declared implicit-solvation model and test sensitivity to dielectric, cavity, ionic strength, and charged-surface assumptions. Use explicit-water or constant-potential checks where they can change the ranking. Evaluate reconstruction, aggregation, dissolution, poisoning, and site blocking under relevant conditions.

Propagate uncertainty from numerical settings, magnetic states, structural alternatives, electrochemical treatment, solvation, thermochemistry, and pathway choice. Report rank stability rather than a single unsupported ordering.

## Stage 6: acceptance and publication release

Update `data/production_campaign_manifest.csv` only with calculation identifiers and statuses backed by raw archives. Update the run ledger, claim-evidence matrix, source-data files, tables, figures, Supporting Information, and manuscript together. Run `scripts/run_validation_suite.py`, the GPAW smoke test, the citation/cross-reference audit, the PDF compilation, and visual inspection from a clean checkout.

No catalyst ranking, mechanism, limiting potential, selectivity claim, or experimental recommendation may enter the manuscript until the relevant evidence rows are accepted. If the complete campaign cannot be executed, submit only the benchmark version and preserve the boundary explicitly.
