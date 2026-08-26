# Citation and cross-reference audit

**Audit status:** PASS

The revised manuscript was checked with `scripts/audit_citations_crossrefs.py` after normalising grouped citations into explicit individual numeric citations.

| Check | Result |
|---|---|
| Citations in abstract | 0 |
| Reference entries | 25 |
| References cited in main text | 25 |
| Uncited references | 0 |
| Missing bibliography numbers | 0 |
| Citation numbering | Sequential 1–25 |
| Table cross-reference mentions | 8 |
| Figure cross-reference mentions | 2 |
| Equation cross-reference mentions | 2 |
| Supporting Information mentions | 1 |

Every reference retained in the bibliography is cited in the main text. The abstract contains no literature citation. Citations are placed in the Introduction, Discussion, strengths and limitations, and future-recommendations sections where the relevant claims are made. The YouTube source is not used as a chemistry reference and is kept only in the article-writing research record.

The manuscript explicitly refers to Table 1 for the model matrix, Table 2 for the structure audit, Table 3 for executed calculation status, Table 4 for the convergence summary, Figure 1 for the real-data diagnostic plot, Equation 1 for the adsorption-energy definition, Equation 2 for the CHE relation, and the Supporting Information for reproducibility details. Full row-level convergence data remain in `data/convergence/convergence.csv` and are identified in the Table 4 caption.

The reference count is within the requested 20–30 range and is not inflated with uncited entries. The final audit must be rerun whenever the manuscript or bibliography changes.
