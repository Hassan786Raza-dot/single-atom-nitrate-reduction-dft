# Article redesign specification

## Chosen article type

The project will be reframed as a **computational reproducibility and numerical-validation benchmark** for nitrate electroreduction modelling on 2D single-atom site models. It will not claim a catalyst ranking or reaction mechanism because those calculations are not present.

## Proposed contribution

The paper's contribution is that it demonstrates, with an executable open-source workflow and archived diagnostics, why a nominal 30-candidate nitrate SAC screen is not scientifically interpretable until model construction, numerical convergence, spin, charge, solvation, and provenance gates are satisfied. The contribution is operational: it supplies a testable audit framework and quantifies the failure of simplistic total-energy convergence tests.

## Research question

Can a matched periodic-DFT workflow distinguish file-valid starting models from chemically and numerically accepted nitrate-reduction results, and which validation gates must be passed before a SAC ranking is defensible?

## Hypothesis

A structure can pass geometric checks while remaining unsuitable for activity ranking because total energies are sensitive to cutoff, k-point sampling, vacuum, support construction, spin, charged-adsorbate treatment, and calculator mode. Therefore, structural validity and numerical validity must be reported as separate gates.

## Evidence hierarchy

1. **Directly measured in this project:** generated structure counts, geometry-audit outcomes, convergence energies/ranges, run-status ledger, code-test outcomes, PDF rendering.
2. **Derived from direct data:** family-wise energy ranges and pass/refine classifications.
3. **Literature-supported context:** nitrate mechanisms, SAC/2D model rationale, CHE, solvation and grand-canonical limitations.
4. **Not evidenced:** catalyst activity ranking, adsorption free energies, transition-state barriers, selectivity, microkinetic rates, or experimental performance.

## New figure/table sequence

- Figure 1: workflow and evidence gates (schematic, no scientific data implied).
- Figure 2: compact real-data convergence benchmark, with a warning that total energies are diagnostics.
- Table 1: model inventory and structural-audit outcomes.
- Table 2: executable environment and calculation-status taxonomy.
- Table 3: convergence data and family ranges.
- Box 1: minimum dataset required before a catalyst-ranking claim.

## Writing rules

Use short, declarative claims. Put a quantitative result in every Results subsection. Do not repeat the computational limitation in every paragraph. Replace “publication-quality convergence figure” with “benchmark figure”. Define `starting structure`, `diagnostic calculation`, `accepted calculation`, and `production result`. Keep the manuscript within a focused full-paper length and move detailed reproducibility commands to supporting information.

## Required additions to the project

- Add a claim-to-evidence matrix.
- Add a journal/guidance synthesis and source classification.
- Add a figure/table inventory with source-data paths.
- Add a production-readiness checklist for future GPAW/VASP runs.
- Replace any title or status text that implies a completed catalyst screen.
