# Figure and table inventory for the high-impact catalyst paper

## Existing evidence-based artefacts

| Artefact | Current content | Evidence source | Status |
|---|---|---|---|
| Table 1 | Proposed matched support/metal starting matrix | Design specification | Valid as a design table; not a catalyst result |
| Table 2 | 96 starting structures and geometry-audit outcome | Geometry-audit records | Valid as input-level evidence |
| Table 3 | Executed GPAW diagnostic status | Run-status ledger | Valid as execution evidence; all current entries are diagnostic-only |
| Table 4 | Compact graphene cut-off, k-point, vacuum, and spin diagnostics | Convergence CSV | Valid as diagnostic evidence; not adsorption convergence |
| Table 5 | Limitation classification and repair pathway | Limitation audit | Valid as evidence-boundary synthesis |
| Figure 1 | Compact graphene total-energy diagnostic plot | Convergence CSV and plotting script | Valid as numerical diagnostic; not catalytic performance |

## Discovery figures that must not be fabricated

The following figures are required for a genuine high-impact catalyst-discovery paper, but they can only be generated after the corresponding calculations are accepted:

1. A relaxed-structure and coordination figure showing all stable SAC motifs and alternative anchoring geometries.
2. A magnetic-state and structural-stability comparison across the 30 SACs.
3. Observable-based convergence plots for representative SACs and adsorbates.
4. A nitrate/H* adsorption-energy and free-energy comparison under a declared electrochemical convention.
5. A solvation and potential-sensitivity figure for ranking-critical states.
6. A complete nitrate-to-ammonia and HER free-energy diagram.
7. Transition-state structures and verified barrier comparisons where kinetically relevant.
8. A limiting-potential, potential-determining-step, and selectivity summary.
9. Coverage/site-blocking and hydrogen-availability sensitivity plots.
10. Stability, reconstruction, aggregation, migration, dissolution, and poisoning summaries.
11. Uncertainty intervals and rank-stability visualisations.

No numerical values, bars, rankings, free-energy curves, or error intervals should be inserted into these figures until their source calculations pass the acceptance gates in `PRODUCTION_CAMPAIGN.md` and are recorded in the production evidence ledgers.

## Publication rule

A polished graphical package cannot substitute for missing chemical evidence. The current figure/table package is complete for the benchmark article. The high-impact discovery figure/table package remains calculation-dependent and must be generated from machine-readable accepted results, not estimated, interpolated, or visually inferred values.
