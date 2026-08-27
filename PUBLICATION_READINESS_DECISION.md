# Publication-readiness decision

## Decision

**No: the project is not ready for publication as a high-impact catalyst-discovery paper.** The current evidence does not support a best-SAC ranking, nitrate adsorption free energies, ammonia selectivity, reaction barriers, limiting potentials, stability under electrochemical conditions, or a complete nitrate-to-ammonia mechanism.

**Conditionally yes: the project is potentially ready for submission as a reproducibility-stage periodic-DFT benchmark and production-readiness framework**, subject to journal fit, independent chemistry review, clean-checkout reproduction, and journal-specific submission checks. This is a different article type and must be presented as such in the title, abstract, cover letter, conclusions, and metadata.

## Evidence supporting the benchmark version

The current package contains 4,996 manuscript words, 25 DOI-validated references all cited in the main text, zero abstract citations, explicit cross-references for Tables 1–5, Figure 1, Equations 1–2, and Supporting Information, 96 audited starting structures, an 11-case diagnostic convergence matrix, a successful periodic GPAW smoke test, raw diagnostic records, a claim-evidence matrix, a 90-row production manifest, a staged production protocol, and a visually inspected 17-page PDF.

The deterministic validation suite passes chemistry utility tests, VASP-input generation tests, geometry audits, reference validation, repair-provenance checks, citation/cross-reference checks, and the final project audit. The repository is synchronised and clean at the latest recorded commit.

## Non-negotiable gates before a catalyst-discovery paper

| Gate | Required evidence |
|---|---|
| Structural validity | Relaxed pristine supports, defects, and all 30 SACs; alternative placements; migration, aggregation, reconstruction, dissolution, and defect stability tests |
| Numerical validity | Observable-based cut-off, k-point, vacuum, slab-size, smearing, force, stress, and electronic-convergence studies on representative SAC and adsorbate systems |
| Magnetic validity | Multiple initial magnetic states for every open-shell metal, with near-degenerate solutions retained and assessed |
| Charge/electrochemical validity | Declared nitrate charge, compensating background, electrostatic correction, reference convention, dipole treatment, and consistency across all species |
| Solvation/interface validity | Implicit-solvation sensitivity and higher-level explicit-water or constant-potential checks where ranking-critical |
| Reaction-network completeness | Nitrate-to-nitrite, nitrite-to-ammonia, oxygen-removal, hydrogenation, ammonia-release, and HER alternatives under matched conditions |
| Kinetic validity | Transition states with verified imaginary modes and connectivity; thermochemical corrections with documented methodology |
| Activity/selectivity | Potential-dependent free energies, limiting potentials, coverage/site-blocking assumptions, HER competition, and a complete selectivity basis |
| Stability | Anchoring, defect formation, reconstruction, aggregation, migration, dissolution, and poisoning analysis under relevant conditions |
| Uncertainty | Sensitivity to numerical settings, spin, structure, solvation, potential, thermochemistry, and pathway assumptions |
| Experimental relevance | A testable synthesis, characterisation, electrochemical protocol, controls, and mass-balance plan if a materials-impact claim is made |

## Current execution boundary

The sandbox has approximately six CPUs and 3.8 GiB RAM. A representative 250 eV Fe@graphene optimisation with a 0.05 eV Å⁻¹ force target was interrupted after six ionic steps because of resource limits; its partial logs are preserved as diagnostic-only. No unsupported result is promoted to the chemical dataset.

The remaining gates must be executed on a suitably resourced workstation or cluster using the archived structures and `PRODUCTION_CAMPAIGN.md`. Until those calculations are completed and accepted, the benchmark framing is the only scientifically valid publication framing.

## Submission recommendation

Submit the current manuscript only to a journal that accepts computational methodology, reproducibility, workflow, or benchmarking studies. Use the benchmark cover letter and Supporting Information. Do not submit it as a conventional new-catalyst or high-throughput activity/selectivity article, and do not imply that a Q1 outcome or acceptance is guaranteed.
