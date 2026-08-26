# Comprehensive limitation and validity audit

## Executive assessment

The project is strongest as an auditable workflow benchmark and weakest as a catalyst-discovery study. The central limitation is not manuscript style alone: the current evidence does not contain converged chemical observables for the 30 SACs. Consequently, the project cannot validly claim a best metal, a preferred support, a nitrate-reduction mechanism, a limiting potential, a selectivity trend, or a free-energy pathway.

The present audit distinguishes three categories. **Repairable limitations** can be corrected by changing code, documentation, cross-references, or presentation. **Analysis-repairable limitations** can be addressed using already archived data, provided the interpretation remains diagnostic. **Calculation-blocked limitations** require new periodic electronic-structure calculations and cannot be repaired by rewriting.

## Limitation matrix

| Limitation | Evidence in project | Category | Required repair |
|---|---|---|---|
| Abstract previously contained citations | Manuscript audit found two abstract citations before correction | Repairable | Remove citations; strict audit now passes with zero abstract citations |
| Bibliography contained references not used in the main text | Strict parser initially found nine uncited entries | Repairable | Place each relevant reference in an applicable main-text section; current audit uses all 25 |
| Figures and tables were not consistently cross-referenced | Several artefacts had captions but no explicit first-use reference | Repairable | Add explicit Table 1–4, Figure 1, Equation 1–2, and Supporting Information references |
| Figure caption duplicated in generated PDF | Visual PDF audit identified automatic and manual caption duplication | Repairable | Separate image syntax from manual caption; final PDF has one caption |
| Main tables were too dense | Visual audit identified cramped status and convergence tables | Repairable | Use compact scientific summaries in the main text and preserve full records in source data/SI |
| Absolute total-energy convergence was treated as a proxy for production readiness | The 11-row graphene benchmark reports large total-energy ranges | Analysis-repairable | Reframe as a diagnostic only; converge adsorption-energy differences, forces, geometries, magnetic states, and free-energy steps in production |
| Only one compact graphene proxy was used for convergence | `data/convergence/convergence.csv` contains graphene settings, not SAC observables | Calculation-blocked | Repeat convergence on representative supports, defects, bare SACs, nitrate, H*, and key intermediates |
| The 30 bare SACs are starting geometries, not optimised structures | Geometry audit validates input files only | Calculation-blocked | Optimise all 30 models with multiple magnetic initialisations and preserve all raw outputs |
| Two plane-wave SAC optimisations failed the declared force criterion | Run-status ledger marks Fe@graphene and Fe@MoS₂ diagnostic-only | Calculation-blocked | Run production-quality optimisations with adequate cut-off, k mesh, slab size, force threshold, and ionic steps |
| One LCAO diagnostic was not comparable with plane-wave calculations | Different calculator mode and settings | Analysis-repairable | Keep separate and label diagnostic-only; never merge energies with plane-wave results |
| Nitrate is charged but production charge treatment is absent | Starting geometries exist; no accepted charged-nitrate results exist | Calculation-blocked | Declare charge, compensating background, electrostatic correction, cell-size test, and reference convention; test charged adsorption and solvation |
| CHE is not sufficient for all nitrate steps | Protocol recognises CHE limits; no potential-dependent production data exist | Calculation-blocked | Use CHE only for appropriate PCET steps and test constant-potential/grand-canonical or equivalent corrections for charge-sensitive steps |
| Solvation and double-layer effects are unresolved | No accepted solvated nitrate or interfacial calculations are archived | Calculation-blocked | Perform implicit-solvation sensitivity and, where ranking-critical, explicit/GC-DFT checks |
| Spin and magnetic-state sampling is incomplete | Closed-shell graphene spin comparison is unchanged; transition-metal states are not validated | Calculation-blocked | Run several initial magnetic moments and retain near-degenerate states for every open-shell metal |
| Defect and SAC structures may reconstruct or aggregate | Starting geometry audit does not test thermodynamic stability | Calculation-blocked | Optimise alternative anchoring geometries and test migration, reconstruction, aggregation, dissolution, and defect formation |
| Reaction network is not executed | No nitrate-to-nitrite, nitrite-to-ammonia, HER, or ammonia-release energetics exist | Calculation-blocked | Define and calculate the complete network, including transition states where ranking-relevant |
| No uncertainty or sensitivity analysis exists for chemical predictions | No accepted chemical predictions exist | Calculation-blocked | Propagate numerical, magnetic, solvation, structural, and pathway uncertainty after production calculations |
| No experiment-facing validation exists | Entire package is computational | Calculation-blocked/claim boundary | Present as prediction only and provide a testable synthesis/characterisation plan; do not imply experimental validation |

## Figure and table provenance audit

**Figure 1** is generated from `data/convergence/convergence.csv` by `scripts/plot_convergence.py`. It displays absolute total-energy diagnostics for cut-off, k-point, and vacuum families and must not be interpreted as an activity, adsorption, or error-bar figure.

**Table 1** is a design table derived from the structure-generation specification. It reports the proposed matched support/metal matrix, not relaxed energies.

**Table 2** is derived from `data/geometry_audit.txt` and `data/adsorbate_geometry_audit.txt`. It reports file and starting-geometry audit outcomes, not thermodynamic stability.

**Table 3** is derived from `data/parsed_run_status.csv` and the archived GPAW run summaries. It reports execution and acceptance status, not catalytic performance.

**Table 4** is derived from `data/convergence/convergence.csv` and `data/convergence/convergence_analysis.md`. It summarises family-wise absolute-energy ranges and diagnostic decisions; the full row-level data remain in the CSV.

**Equations 1 and 2** are methodological definitions: the neutral adsorption-energy bookkeeping convention and the CHE proton–electron chemical-potential convention. They are not fitted equations and do not constitute calculated reaction results.

## Impact assessment

The project can become impactful by making a methodological contribution that prevents invalid high-throughput claims: it demonstrates, with a concrete nitrate-SAC workflow, that structural validity, numerical convergence, magnetic-state selection, electrochemical charge treatment, solvation, stability, and provenance are separate gates. This is a credible and useful contribution if presented as a benchmark and reporting framework.

It cannot become an impactful catalyst-discovery paper through prose alone. A high-impact materials claim requires new accepted chemical evidence: converged SAC energetics, potential- and solvation-aware nitrate chemistry, competing HER, a complete reaction network, stability under relevant conditions, uncertainty analysis, and an experimentally testable prediction. These requirements are consistent with recent constant-potential nitrate work, which shows that nitrate adsorption and dissociation can depend on electrode potential and that CHE-like approximations may differ substantially from grand-canonical results [1], and with reviews documenting that electrocatalytic active sites can reconstruct under potential and reaction environments [2].

## Required manuscript positioning

The title, abstract, introduction, results, discussion, limitations, and conclusions should all identify the work as a reproducibility-stage periodic-DFT benchmark. The novelty should be stated as an evidence-gated readiness framework, not as the discovery of a new catalyst. All tables and figures should be introduced before or at first use, and every numerical statement should trace to a machine-readable source file or a clearly identified literature citation.

## Sources

[1] Sweeney, D. M.; Tran, B.; Goldsmith, B. R. *A grand canonical study of the potential dependence of nitrate adsorption and dissociation across metals and dilute alloys*. **Communications Chemistry** 8, 182 (2025). https://doi.org/10.1038/s42004-025-01579-y

[2] Ning, M. et al. *Dynamic Active Sites in Electrocatalysis*. **Angewandte Chemie International Edition** 63, e202415794 (2024). https://doi.org/10.1002/anie.202415794
