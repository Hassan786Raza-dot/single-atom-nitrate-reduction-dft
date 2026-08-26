# Production-readiness checklist

## Model and structure gates

- [ ] Pristine support is relaxed and its cell treatment is converged.
- [ ] Defect formation and alternative defect structures are assessed.
- [ ] Multiple metal placements and coordination motifs are considered.
- [ ] Metal migration, aggregation, and reconstruction are checked.
- [ ] Bare SAC geometry and spin state are fully relaxed and archived.

## Numerical gates

- [ ] Cutoff convergence is assessed using energy differences and forces.
- [ ] k-point convergence is assessed for the actual slab and observable.
- [ ] Vacuum and dipole corrections are converged.
- [ ] Slab-size or lateral-separation convergence is assessed.
- [ ] Smearing and electronic convergence are documented.
- [ ] Multiple magnetic initialisations are tested for open-shell sites.
- [ ] Final forces and stress satisfy declared thresholds.

## Electrochemical gates

- [ ] Nitrate charge and compensating-background convention are specified.
- [ ] Adsorption reference state is chemically consistent.
- [ ] Solvation model, dielectric, cavity, and ionic conditions are recorded.
- [ ] CHE potential convention is defined and applied only to appropriate PCET steps.
- [ ] Potential-dependent adsorption or charging is checked where relevant.
- [ ] Explicit-water or higher-level checks are performed for shortlisted states.

## Mechanism and selectivity gates

- [ ] Nitrate-to-nitrite and nitrite-to-ammonia alternatives are included.
- [ ] Competing HER steps are evaluated.
- [ ] Transition states have one relevant imaginary mode and connectivity checks.
- [ ] Thermochemical corrections have a documented basis.
- [ ] Stability, dissolution, aggregation, and poisoning risks are assessed.
- [ ] Any descriptor or microkinetic model is tested against the complete network.

## Provenance and publication gates

- [ ] Every result has a calculation identifier and raw-output archive.
- [ ] Every table and figure has a source-data file and regeneration script.
- [ ] Failed and non-converged calculations are retained and labelled.
- [ ] Code, environment, datasets, and licences are documented.
- [ ] Claims in the manuscript are mapped to the claim-evidence matrix.
- [ ] The target journal's article type, reference style, figure rules, and data policy are satisfied.
