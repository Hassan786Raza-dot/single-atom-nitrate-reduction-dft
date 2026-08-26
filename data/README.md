# Data conventions

All CSV files use UTF-8 encoding and comma delimiters. `NR` means not reported or not available; it is not zero. `CALCULATED` records require a calculation identifier and a path to the archived input/output. `LITERATURE` records require a DOI or stable publisher URL. Energies are reported in eV unless a column explicitly states another unit.

## Required provenance fields

| Field | Meaning |
|---|---|
| `record_type` | `CALCULATED`, `LITERATURE`, or `DERIVED` |
| `calculation_id` | Unique identifier for the source calculation |
| `structure_path` | Relative path to the geometry used |
| `software_version` | Code and version used to produce the value |
| `method_label` | Functional, dispersion, basis/cutoff, k-points, spin, and solvent label |
| `audit_status` | `PENDING`, `PASSED`, or `FAILED` |

No final ranking should be produced from records with `audit_status != PASSED`.
