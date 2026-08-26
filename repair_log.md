# Repair log

## Repairs completed

The manuscript and repository were repaired in the following ways:

| Repair | Implementation | Verification |
|---|---|---|
| Stale word-count/status metadata | Updated `PROJECT_STATUS.md` to 4,996 words, five main-text tables, one figure, and 17-page PDF | Final audit pass |
| Production checklist ambiguity | Rewrote `production_readiness_checklist.md` with completed and calculation-blocked gates | Manual review and repository checks |
| Incomplete claim provenance | Extended `claim_evidence_matrix.csv` to 20 rows covering every table, figure, equation, and limitation synthesis | `scripts/validate_repairs.py` pass |
| Missing limitation synthesis in article | Added Table 5 and explicit repair classifications to the manuscript | PDF compilation and manuscript audit |
| Weak interpretation of convergence data | Kept absolute-energy ranges as diagnostics only and specified observable-based production convergence requirements | Manuscript and `limitation_audit.md` |
| Incomplete figure/table provenance | Added source-data and regeneration paths for Tables 1–5 and Figure 1 | Claim matrix and cross-reference audit |
| Citation architecture | Retained zero abstract citations, 25 main-text-used references, and sequential citations | `scripts/audit_citations_crossrefs.py` pass |
| Calculation status overclaim risk | Preserved diagnostic-only labels and prohibited promotion of failed/coarse runs | Project execution rule and claim matrix |

## Remaining calculation-blocked limitations

The following cannot be repaired by documentation or rewriting: production-quality relaxation of all 30 SACs; observable-based cut-off, k-point, vacuum, and slab-size convergence; multiple magnetic states; charged nitrate and compensating-background treatment; solvation and double-layer effects; potential-dependent energetics; complete nitrate-to-ammonia and HER networks; transition states; thermochemistry; stability and reconstruction; uncertainty; and catalyst ranking.

The project therefore remains a scientifically honest benchmark and production-readiness framework. The repair is complete at the repository, interpretation, provenance, and manuscript levels; a catalyst-discovery claim remains blocked until the listed calculations are executed and archived.
