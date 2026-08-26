# DFT-Guided Computational Screening of Single-Atom Catalysts on 2D Materials for Nitrate-to-Ammonia Electroreduction

This repository contains a reproducible research framework for studying the relationship between metal–support interactions, aqueous solvation, and nitrate-to-ammonia electrocatalysis on two-dimensional materials.

## Research objectives

The project is designed to compare isolated transition-metal sites on graphene-derived nitrogen-coordinated carbon, 2H-MoS₂, and g-C₃N₄. It will quantify structural stability, nitrate and intermediate adsorption, proton-coupled electron-transfer thermochemistry, competition with hydrogen evolution, and descriptor–activity relationships.

## Scope and status

The repository currently contains the project specification, an initial evidence-based literature dataset, the methodological design, input-generation and analysis utilities, tests, and audit documentation. Numerical DFT results are not populated unless they are traceable to an executed calculation with archived inputs, outputs, software versions, and convergence checks. No calculated value is presented as an experimental or published result.

A complete publication-grade study requires access to a periodic plane-wave or localised-orbital DFT code, adequate computational resources, and an independently verified electrochemical modelling workflow. The code in this repository is therefore structured to support staged screening rather than to imply that unavailable calculations have already been run.

## Methodology overview

The planned workflow is: (i) systematic literature curation; (ii) support and metal selection; (iii) periodic structure construction; (iv) spin-polarised geometry optimisation; (v) adsorption and reaction-energy calculations; (vi) solvation and thermochemical corrections; (vii) CHE and, where feasible, constant-potential validation; (viii) descriptor, stability, HER, and selectivity analyses; and (ix) cross-checked reporting.

## Reproducibility principles

Every numerical result must be linked to a structure, input file, code version, calculation identifier, and audit record. Literature-derived quantities are labelled as such. Missing or incompatible information is recorded as `NR` rather than inferred. The repository does not claim completion of calculations that have not been executed and independently checked.

## Repository layout

| Directory | Purpose |
|---|---|
| `literature_review/` | Literature dataset, search protocol, and synthesis |
| `scripts/` | Structure, input, parsing, thermochemistry, CHE, and plotting utilities |
| `structures/` | Initial, optimised, and transition-state geometries |
| `data/` | Machine-readable calculated and literature-derived data |
| `electronic_structure/` | Charges, projected densities of states, and spin analyses |
| `figures/` | Reproducible plots and final figures |
| `tables/` | Manuscript-ready tables |
| `manuscript/` | Manuscript source and supporting text |
| `supporting_information/` | Supplementary methods, inputs, and validation material |

## Timeline

The work is organised into literature review, protocol development, structure generation, energetics, descriptor analysis, reporting, and final quality control. The timeline is a planning framework; actual completion depends on access to validated DFT software and sufficient compute time.

## Citation

The literature records in this repository should be cited by DOI or publisher URL. The project itself is released with a permissive open-source code licence, while individual articles remain subject to their publishers' licences.
