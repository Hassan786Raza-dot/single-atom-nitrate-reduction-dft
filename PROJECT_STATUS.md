# Project Status

## Current status (27 August 2026)

The repository and manuscript have undergone repeated audits covering structures, geometry records, convergence data, run ledgers, chemistry utilities, VASP-compatible input generation, citations, tables, figures, equations, manuscript claims, limitations, and PDF rendering. The current manuscript contains **4,996 words**, **25 DOI-validated references**, **five main-text tables**, and one real-data convergence figure. The LaTeX source compiles with XeLaTeX to a **17-page PDF with zero fatal errors**.

The package is publication-formatted as a **reproducibility-stage periodic-DFT benchmark and production-readiness framework**. It is not a completed 30-catalyst activity/selectivity study. The production DFT matrix, charged nitrate/solvation calculations, transition states, free-energy pathway, stability metrics, uncertainty analysis, and catalyst ranking remain unexecuted and are explicitly marked as calculation-blocked.

## Verified completed work

The open-source route is GPAW 24.1.0 with ASE, Ubuntu PAW datasets, and a NumPy/SciPy-compatible isolated runtime. A periodic graphene smoke calculation completed successfully. Three support families were generated: nitrogenated graphene, a 2H-MoS₂ sulphur-vacancy model, and a labelled g-C₃N₄-like starting model. The repository contains 36 audited pristine/defect/bare-SAC structures and 60 audited nitrate/hydrogen starting geometries.

An 11-case compact convergence matrix covering cut-off, k-point mesh, vacuum, and spin settings was executed. The audit flags cut-off, k-point, and vacuum ranges for refinement and restricts the unchanged spin result to the closed-shell graphene benchmark. A machine-readable run-status ledger tracks every executed calculation. Figure 1 and Tables 1–5 are generated or derived from archived project records, with source files and regeneration paths identified in the manuscript and audit reports.

The manuscript now contains zero abstract citations, 25 references all cited in the main text, sequential individual citation numbers, explicit cross-references to Tables 1–5, Figure 1, Equations 1–2, and Supporting Information, and repeated but bounded novelty statements. The complete citation and cross-reference audit passes.

## Calculation-blocked work

The complete 30-model optimisation matrix, adsorption energies, charged-nitrate calculations, solvation and double-layer corrections, potential-dependent energetics, transition states, free-energy diagrams, stability metrics, selectivity analysis, uncertainty analysis, and catalyst ranking are not scientifically accepted. The current sandbox has six CPUs and approximately 3.8 GiB RAM; the 4 × 4 slabs, particularly the 129-atom g-C₃N₄-like models, require substantially more compute for converged spin-polarised production optimisation.

## Execution rule

No numerical result is promoted into the final dataset unless the calculation reaches the declared convergence criteria, has a complete raw-output archive, passes geometry and spin checks, and uses settings supported by the relevant observable-based convergence study. Coarse diagnostics remain explicitly labelled as diagnostic-only.

## Next executable production stage

Run the 30 SAC optimisations on a suitably resourced CPU cluster or connected workstation using the archived structures and GPAW/VASP-compatible input policies. Then repeat adsorption and pathway calculations for shortlisted systems, including consistent charged-nitrate treatment, solvation sensitivity, thermochemistry, electrochemical-potential validation, HER competition, stability, and uncertainty analysis.
