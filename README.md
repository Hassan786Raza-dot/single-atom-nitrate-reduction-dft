# A reproducible periodic-DFT benchmark for nitrate electroreduction on two-dimensional single-atom sites

This repository contains an auditable computational benchmark and production-readiness workflow for modelling nitrate electroreduction on two-dimensional single-atom-site models. It is designed around a central distinction: a geometrically valid starting structure is not automatically a converged, electrochemically meaningful catalyst result.

## Contribution and current scope

The project evaluates the workflow required before a matched 30-model SAC comparison can support mechanistic or catalyst-ranking claims. It generates nitrogenated graphene, sulphur-vacancy 2H-MoS₂, and labelled g-C₃N₄-like starting models with ten metal identities. It records a compact periodic-DTF convergence benchmark, executable GPAW diagnostics, structure audits, input-generation utilities, and a claim-to-evidence matrix.

The current package contains 36 support/reference and bare-SAC starting structures and 60 nitrate/hydrogen starting structures. All pass the defined input-level geometry audit. An eleven-calculation graphene benchmark exposes sensitivity to cut-off, k-point mesh, and vacuum. These results are diagnostics; they are not adsorption energies, reaction barriers, activity values, or selectivity rankings.

## Scientific boundary

The repository does not claim that any candidate is the best nitrate-reduction catalyst. It does not contain an accepted 30-SAC production matrix, converged nitrate adsorption free energies, charged/solvated nitrate thermochemistry, transition states, complete free-energy pathways, microkinetic rates, or experimental validation. These omissions are deliberately recorded. The project must not be cited as evidence for a catalyst ranking until those calculations are executed and audited.

## Software route

Executed diagnostics use open-source GPAW 24.1.0 and ASE with registered Ubuntu PAW datasets. VASP-compatible POSCAR, INCAR, KPOINTS, and POTCAR-manifest generation is included, but proprietary VASP software and potentials are not redistributed. The exact environment, dataset path, and status rules are documented in `ENVIRONMENT.md` and `supporting_information/supporting_information.md`.

## Reproducibility controls

Every numerical record must be linked to a structure, input, code and dataset version, calculation identifier, raw output, convergence state, and audit record. Status values distinguish `INPUT_ONLY`, `DIAGNOSTIC_ONLY`, `ACCEPTED`, and `NOT_RUN`. Missing data are not inferred. The final claim-to-evidence matrix prohibits unsupported activity, pathway, and selectivity claims.

## Key documents

| File | Purpose |
|---|---|
| `manuscript/manuscript.md` | Redesigned benchmark manuscript |
| `manuscript/manuscript.pdf` | XeLaTeX-rendered manuscript |
| `supporting_information/supporting_information.md` | Reproduction and audit details |
| `article_writing_research.md` | Research-article writing and reporting guidance synthesis |
| `project_quality_gap_analysis.md` | Whole-project standards-based critique |
| `article_redesign_spec.md` | New article contribution and structure |
| `comprehensive_audit_report.md` | Earlier full scientific and publication audit |
| `claim_evidence_matrix.csv` | Claim-level evidence controls |
| `figure_table_inventory.md` | Source-data and visualisation inventory |
| `production_readiness_checklist.md` | Gates for future production DFT |
| `journal_guidelines_audit.md` | Publisher and journal requirements |

## Reproduction commands

From the repository root, generate structures with `python3 scripts/generate_structures.py` and `python3 scripts/generate_adsorbates.py`; audit them with `python3 scripts/audit_geometries.py`; analyse the convergence benchmark with `python3 scripts/analyse_convergence.py`; and run the final project audit with `python3 scripts/final_audit.py`. The direct tests are `python3 scripts/tests/test_chemistry_utils.py` and `python3 scripts/tests/test_vasp_inputs.py`.

## Licence and citation

The workflow code and documentation are released under the repository's open-source terms. GPAW and ASE retain their own licences, and individual literature articles remain subject to publisher copyright. Cite the DOI records in `references/manuscript_references.md` when reusing literature context, and cite the repository commit when reusing the workflow or benchmark data.
