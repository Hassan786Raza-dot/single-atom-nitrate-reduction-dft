# Figure and table inventory

| Item | Type | Source data | Current status | Permitted interpretation |
|---|---|---|---|---|
| Figure 1 | Convergence plot | `data/convergence/convergence.csv` | Complete and regenerated | Numerical diagnostic only |
| Table 1 | Model inventory | `system_selection.md`; structure generator | Complete | Starting-model design |
| Table 2 | Geometry audit | `data/geometry_audit.txt`; `data/adsorbate_geometry_audit.txt` | Complete | Input-file validity |
| Table 3 | Convergence table | `data/convergence/convergence.csv` | Complete | Benchmark sensitivity |
| Table 4 | Run-status ledger | `data/parsed_run_status.csv` | Complete | Execution provenance; not activity |
| Future Figure A | Stability map | `data/stability.csv` | Not generated | Must not be created until calculations exist |
| Future Figure B | Adsorption descriptor map | `data/adsorption.csv` | Not generated | Must use accepted adsorption results only |
| Future Figure C | Free-energy pathway | `data/reaction_steps.csv` | Not generated | Must include charge, solvation, CHE, and reference details |
| Future Figure D | Microkinetic/selectivity map | `data/microkinetics.csv` | Not generated | Requires validated reaction network and rate model |

## Figure audit rule

A figure may enter the manuscript only when a machine-readable source-data file, a reproducible plotting script, units, a caption, and an audit record exist. No planned figure should be represented by a placeholder that looks like a completed result.

## Table audit rule

A reported numerical table must contain calculation identifiers, units, calculator mode, software/dataset version, convergence status, and a link to the raw-output directory. Missing values must be represented as `NOT_RUN`, `FAILED`, or `NOT_APPLICABLE`, never as blank cells that could be mistaken for zero.
