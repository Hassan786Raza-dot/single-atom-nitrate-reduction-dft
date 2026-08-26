# Comprehensive second-pass scientific and publication audit

**Audit date:** 27 August 2026

## Executive finding

The repository and expanded manuscript were audited a second time. The corrected manuscript contains 5,299 words in the Markdown source, 25 reference entries, 25 DOI links that resolve through Crossref, 4 embedded Markdown tables, and one embedded convergence figure. A subsequent generated LaTeX source compiles successfully with XeLaTeX to a 17-page PDF with no fatal errors, missing image errors, or missing chemical-symbol errors.

The package is internally coherent as a **reproducibility-stage benchmark/workflow manuscript**. It is not scientifically valid to present it as a completed catalyst-discovery paper because the 30-model production optimisation matrix, converged adsorption energetics, solvation-aware charged nitrate calculations, transition states, free-energy pathway, and catalyst ranking are not present. The manuscript now states this limitation repeatedly and does not report unsupported activity or selectivity conclusions.

## Artefact-by-artefact audit

| Artefact class | Audit performed | Finding | Action |
|---|---|---|---|
| Structures | Read-back, cell/vacuum/contact checks | 36 bare/support structures and 60 adsorbate inputs pass the current geometry audit | Retained; starting structures are clearly labelled as non-results |
| Convergence data | CSV-to-table comparison | 11 calculation rows are reproduced with rounded values consistent with `data/convergence/convergence.csv` | Retained; values are interpreted only as numerical diagnostics |
| Run ledger | Parser output checked against manuscript | Archived GPAW runs are separated by mode and acceptance status | Retained; diagnostic-only classification preserved |
| Chemistry utilities | Standalone tests and Python compilation | Adsorption-energy, CHE, limiting-potential, CSV, and ORCA-input utilities pass existing direct tests | Retained; utilities are explicitly not quantum calculations |
| VASP generator | Standalone test and source inspection | Generates POSCAR/INCAR/KPOINTS and a non-proprietary POTCAR manifest | Retained; no proprietary VASP assets claimed |
| Literature | DOI resolution and metadata cross-check | 25 manuscript DOI links resolve through Crossref; one legacy CSV DOI (`10.1021/acsenergylett.2c01975`) returns 404 and is excluded from the manuscript bibliography | Added DOI audit files; invalid legacy record flagged |
| Figures | Source/data path and PDF rendering | Convergence figure loads into the PDF and is sourced from the executed convergence data | Retained; no unvalidated ranking plots included |
| Tables | Source comparison and PDF visual inspection | Tables are complete and readable; some cells remain dense and produce nonfatal LaTeX overfull-box warnings | Shortened headers/cells and added layout header; further journal-template typesetting may still be needed |
| Equations | Markdown-to-LaTeX conversion and PDF inspection | Adsorption-energy and CHE equations render as display mathematics | Corrected equation delimiters; compiled successfully |
| Manuscript | Word count, citation count, sections, claims | 5,299 words, 25 references, standard sections, explicit limitations, and data-availability discussion | Expanded and corrected |
| PDF | XeLaTeX compilation and visual inspection | 17 pages, no fatal compile errors, no missing figure, no missing chemical-symbol failures | Rendering verified |

## Scientific validity findings

The adsorption-energy sign convention is internally consistent with the stated equation, but the manuscript correctly warns that gas-phase, aqueous, solvated-ion, and CHE references cannot be mixed. The CHE expression is appropriate as a first-pass convention when the electrode-potential reference is defined consistently; it is not presented as a complete constant-potential treatment. The manuscript correctly separates total-energy convergence diagnostics from convergence of adsorption or reaction-energy differences.

The nitrate charge problem is correctly identified as a central limitation. The generated nitrate structures are inputs, not aqueous adsorption results. No unsupported nitrate adsorption energy, ammonia free-energy diagram, limiting potential, or selectivity ranking appears in the revised manuscript. The role of solvation, compensating charge, potential dependence, and grand-canonical methods is described as a required production-stage validation rather than falsely claimed to have been completed.

The spin discussion is appropriately limited. The closed-shell graphene spin test is not used to validate Fe, Co, Ni, or other open-shell transition-metal magnetic states. The support models are labelled as reproducible starting models rather than universal experimental structures. The manuscript also distinguishes isolated-atom binding from true resistance to aggregation, dissolution, reconstruction, or vacancy instability.

The main scientific weakness remains evidentiary completeness rather than a hidden algebraic error: the completed calculations are diagnostic and the convergence benchmark is not sufficient to select production settings for the full SAC matrix. This limitation is retained as the central conclusion.

## Citation audit

The manuscript contains 25 references. Crossref returned HTTP 200 metadata for all 25 DOI records used in the manuscript. The bibliography includes the key Fe-SAC nitrate study, active-hydrogen work, atomically dispersed M–N–C study, nitrate-reduction descriptor/microkinetic papers, single-atom and 2D-support reviews or design papers, CHE foundations, implicit-solvation methodology, and constant-potential/grand-canonical studies. The invalid legacy DOI identified in the original 11-row CSV is not used in the revised manuscript.

The bibliography uses abbreviated author lists for some papers. This is bibliographically acceptable only if the final target journal permits `et al.` in the reference list; the final submission should be passed through the selected journal's exact reference style. DOI resolution establishes record existence and metadata, not that every interpretive statement is fully supported. Claims in the revised text have therefore been narrowed to the findings directly relevant to the cited sources.

## Journal-alignment audit

The manuscript follows the common requirements identified from official Nature Communications, Communications Chemistry, ACS, and Journal of Materials Chemistry A guidance: standard scientific sections, a clear title and abstract, complete computational methods, embedded tables/figure, supporting information, data/code availability discussion, and explicit limitations. The topic is more naturally positioned as a computational-methodology or reproducibility benchmark unless the missing production calculations are completed. A conventional catalyst-ranking submission to a Q1 journal would be rejected or returned for lack of converged activity/selectivity evidence.

## Rendering audit

The expanded Markdown manuscript was converted to LaTeX using Pandoc and compiled twice with XeLaTeX. The final PDF has 17 pages in US-letter geometry. No fatal errors, missing image files, or missing Unicode chemical symbols were detected. The convergence figure appears in the PDF. Nonfatal overfull/underfull box warnings remain, mainly in dense tables and long DOI/reference lines. These are layout warnings rather than scientific errors; a final journal-template pass should address them with the journal's class file, table-width controls, and reference style.

## Reproducibility status

The repository contains the source manuscript, generated LaTeX source, compiled PDF, supporting information, input generators, structure generators, geometry audits, convergence scripts, plot script, DOI validators, final audit script, environment documentation, raw diagnostic outputs, parsed run ledger, and audit notes. The project has a clean separation between raw calculation artefacts, processed records, and manuscript prose.

## Final verdict

**Pass:** reproducibility-stage benchmark/workflow package; manuscript length; 25-reference minimum; DOI resolution; source/table/figure linkage; equation rendering; structural audit; code compilation; direct unit-test entry points; transparent limitations.

**Not yet a pass:** completed Q1 catalyst-discovery research paper. The missing items are genuine production calculations, not formatting tasks: converged 30-SAC optimisations, consistent nitrate/H adsorption, charged-cell and solvation checks, pathway intermediates, transition states, thermochemistry, stability and aggregation tests, and a validated selectivity/rate analysis.
