# Computational Materials Science submission metadata

## Proposed title

**An auditable periodic-DFT benchmark and production-readiness framework for nitrate-reduction single-atom catalyst screening**

## Article type

Research article. The manuscript should be presented as a computational-materials methodology and reproducibility benchmark, not as a completed catalyst-performance ranking.

## Scope statement for submission

This manuscript addresses computational materials science through an executable, auditable workflow for two-dimensional supports and single-atom catalyst starting models. Its contribution is the separation of structural, numerical, electrochemical, execution, and provenance gates before interpreting a high-throughput catalyst screen. The repository provides FAIR-oriented source structures, audit scripts, diagnostic convergence records, runtime information, and reproducibility documentation.

## Highlights

- Auditable workflow separates structural validity from catalytic interpretation.
- Ninety-six periodic support, SAC, and adsorbate starting structures are audited.
- Eleven GPAW convergence diagnostics quantify compact-model sensitivity.
- Claim-to-evidence mapping prevents unsupported catalyst-ranking conclusions.
- Open-source inputs, tests, provenance, and production gates are released.

## Graphical-abstract specification

The graphical abstract should be generated as a clean vector-style workflow diagram, not as a catalyst-performance claim. It should show: matched support/SAC/adsorbate inputs; structural audit; numerical and magnetic gates; charge/solvation/potential gates; raw-output provenance; and the final decision branch labelled either `ACCEPTED FOR CHEMICAL INTERPRETATION` or `REQUIRES FURTHER CALCULATION`. It must not show a numerical catalyst ranking, free-energy curve, or selectivity value because those results are not present in the accepted dataset.

## Research-data statement

All executable scripts, starting structures, audit records, diagnostic convergence data, calculation-status records, production manifests, and provenance documentation are available in the public repository:

https://github.com/hassanraza147/single-atom-nitrate-reduction-dft

Proprietary VASP executables and PAW potential files are not distributed. The repository provides VASP-compatible input-generation policies and a GPAW-based open-source execution route. Production calculations marked `NOT_RUN` or `DIAGNOSTIC_ONLY` are not presented as accepted chemical results.

## Declarations to complete before submission

- Declaration of competing interests: authors must complete the journal’s required statement.
- Funding statement: authors must provide the actual funding information or state that no specific funding was received.
- Author contributions: authors must provide the actual contribution statement.
- Data and code availability: use the repository statement above, with an archival DOI added if available.
- Submission declaration: confirm that the manuscript is not under consideration elsewhere and has not been published previously.
- Ethics and permissions: confirm that all figures, data, and code are owned by the authors or appropriately licensed.

## File checklist

| File | Submission role | Status |
|---|---|---|
| `manuscript/manuscript.pdf` | Review manuscript | Prepared; final journal portal conversion may be required |
| `manuscript/manuscript.md` | Source manuscript | Repository source |
| `manuscript/supporting_information.md` | Supplementary material source | Prepared; convert to the journal’s accepted supplementary format |
| `manuscript/cover_letter_benchmark.md` | Cover letter | Prepared; adapt the editor and journal name |
| `manuscript/cms_submission_metadata.md` | Title, highlights, data statement, and checklist | Prepared |
| `figures/final/convergence_benchmark.png` | Figure 1 | Evidence-based diagnostic figure |
| `data/` and `scripts/` | Data/code repository | Public and auditable |

## Editorial boundary

The journal’s official guide states that computational-materials submissions must provide originality and scientific merit, and that methodologically focused work should provide FAIR-compatible data and code. No journal can guarantee acceptance. The present manuscript should be submitted only with the benchmark framing and only after authors complete the declarations and final portal-specific checks.
