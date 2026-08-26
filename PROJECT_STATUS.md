# Project Status

## Verified completed work

The open-source route is GPAW 24.1.0 with ASE, Ubuntu PAW datasets, and a NumPy/SciPy-compatible isolated runtime. A periodic graphene smoke calculation completed successfully. Three support families were generated: nitrogenated graphene, a 2H-MoS₂ sulphur-vacancy model, and a labelled g-C₃N₄-like starting model. The repository contains 36 audited pristine/defect/bare-SAC structures and 60 audited nitrate/hydrogen starting geometries.

An 11-case compact convergence matrix covering cutoff, k-point mesh, vacuum, and spin settings was executed. The audit correctly flags cutoff, k-point, and vacuum ranges for refinement; only the compact spin comparison passed the provisional tolerance. A coarse Fe@graphene plane-wave optimisation was executed and its raw output is archived, but it did not meet the requested final force criterion and is not accepted as a production result.

## Not yet publication-grade

The complete 30-model optimisation matrix, adsorption energies, solvation corrections, transition states, free-energy diagrams, stability metrics, selectivity analysis, and manuscript results are not yet scientifically accepted. The current sandbox has six CPUs and approximately 3.8 GiB RAM; the generated 4 × 4 periodic slabs, especially the 129-atom g-C₃N₄-like models, require substantially more compute for converged spin-polarised plane-wave optimisation. Running an incomplete or coarse batch would not satisfy a Q1 publication standard.

## Execution rule

No numerical result is promoted into the final dataset unless the calculation reaches the declared convergence criteria, has a complete raw-output archive, passes geometry and spin checks, and uses settings supported by the convergence study. Coarse diagnostics remain explicitly labelled as such.

## Next required computational stage

Run the 30 SAC optimisations on a suitably resourced CPU cluster or connected workstation using the archived structures and the GPAW/VASP-compatible input policies. Then repeat adsorption and pathway calculations for shortlisted systems, including consistent charged-nitrate treatment, solvation sensitivity, thermochemistry, and electrochemical-potential validation.
