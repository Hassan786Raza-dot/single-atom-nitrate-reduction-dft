# Project Status

## Second-pass audit status (27 August 2026)

The repository and manuscript have undergone a second independent audit covering structures, geometry records, convergence data, run ledgers, chemistry utilities, VASP input generation, citations, tables, figures, equations, manuscript claims, and PDF rendering. The revised manuscript contains 5,299 words, 25 DOI-validated references, four embedded tables, and the real-data convergence figure. The LaTeX source compiles with XeLaTeX to a 17-page PDF with no fatal errors or missing figures. A detailed record is provided in `comprehensive_audit_report.md`.

The package passes as a reproducibility-stage benchmark/workflow manuscript. It does not pass as a completed 30-catalyst activity/selectivity study because the production DFT matrix, charged nitrate/solvation calculations, transition states, free-energy pathway, and catalyst ranking remain unexecuted. These are explicitly marked as pending rather than represented by fabricated values.

## Verified completed work

The open-source route is GPAW 24.1.0 with ASE, Ubuntu PAW datasets, and a NumPy/SciPy-compatible isolated runtime. A periodic graphene smoke calculation completed successfully. Three support families were generated: nitrogenated graphene, a 2H-MoS₂ sulphur-vacancy model, and a labelled g-C₃N₄-like starting model. The repository contains 36 audited pristine/defect/bare-SAC structures and 60 audited nitrate/hydrogen starting geometries.

An 11-case compact convergence matrix covering cutoff, k-point mesh, vacuum, and spin settings was executed. The audit correctly flags cutoff, k-point, and vacuum ranges for refinement. A machine-readable run-status ledger (`data/parsed_run_status.csv`) tracks every executed calculation. A publication-quality convergence figure and diagnostic table are complete.

A transparent manuscript (`manuscript/manuscript.md`, `.tex`, and `.pdf`) and supporting-information document are complete. They report the reproducibility baseline, verified workflow, and numerical sensitivities while explicitly separating diagnostic findings from the unexecuted full SAC reaction study.

## Not yet publication-grade

The complete 30-model optimisation matrix, adsorption energies, solvation corrections, transition states, free-energy diagrams, stability metrics, selectivity analysis, and catalyst ranking are not yet scientifically accepted. The current sandbox has six CPUs and approximately 3.8 GiB RAM; the 4 × 4 slabs, particularly the 129-atom g-C₃N₄-like models, require substantially more compute for converged spin-polarised plane-wave optimisation. Running an incomplete or coarse batch would not satisfy a Q1 publication standard.

## Execution rule

No numerical result is promoted into the final dataset unless the calculation reaches the declared convergence criteria, has a complete raw-output archive, passes geometry and spin checks, and uses settings supported by the convergence study. Coarse diagnostics remain explicitly labelled as such.

## Next required computational stage

Run the 30 SAC optimisations on a suitably resourced CPU cluster or connected workstation using the archived structures and the GPAW/VASP-compatible input policies. Then repeat adsorption and pathway calculations for shortlisted systems, including consistent charged-nitrate treatment, solvation sensitivity, thermochemistry, and electrochemical-potential validation.
