# Production-readiness checklist

The checklist distinguishes completed reproducibility gates from calculation-blocked production gates. A checked item is supported by archived project evidence; an unchecked item requires new scientific calculations or external validation.

## Model and structure gates

- [x] Pristine, defect, and reference support starting structures are generated and read back successfully.
- [ ] Pristine support is relaxed and its cell treatment is converged for production observables.
- [ ] Defect formation and alternative defect structures are assessed energetically.
- [ ] Multiple metal placements and coordination motifs are compared after relaxation.
- [ ] Metal migration, aggregation, reconstruction, and dissolution are checked.
- [ ] Bare SAC geometry and spin state are fully relaxed and accepted for all 30 models.

## Numerical gates

- [x] A compact graphene diagnostic has tested cut-off, k-point, vacuum, and closed-shell spin settings.
- [ ] Cut-off convergence is assessed using adsorption-energy differences and forces for representative SACs.
- [ ] k-point convergence is assessed for the actual support/SAC slabs and target observables.
- [ ] Vacuum and dipole corrections are converged for charged and neutral adsorbates.
- [ ] Slab-size or lateral-separation convergence is assessed.
- [ ] Smearing and electronic convergence are documented for every production calculation.
- [ ] Multiple magnetic initialisations are tested for every open-shell metal.
- [ ] Final forces and stress satisfy declared production thresholds.

## Electrochemical gates

- [ ] Nitrate charge and compensating-background convention are specified and tested.
- [ ] Adsorption reference states are chemically consistent across all species.
- [ ] Solvation model, dielectric, cavity, ionic conditions, and charged-surface treatment are recorded.
- [x] The CHE potential convention is defined in Equation 2.
- [ ] CHE is applied only to appropriate proton–electron-transfer steps.
- [ ] Potential-dependent adsorption or charging is checked where relevant.
- [ ] Explicit-water or higher-level checks are performed for shortlisted states.

## Mechanism and selectivity gates

- [ ] Nitrate-to-nitrite and nitrite-to-ammonia alternatives are calculated.
- [ ] Competing HER steps are evaluated on the same sites and reference convention.
- [ ] Transition states have one relevant imaginary mode and connectivity checks.
- [ ] Thermochemical corrections have a documented vibrational or approximation basis.
- [ ] Stability, dissolution, aggregation, reconstruction, and poisoning risks are assessed.
- [ ] Any descriptor or microkinetic model is tested against the complete reaction network.

## Provenance and publication gates

- [x] Every executed diagnostic has a calculation identifier and raw-output archive.
- [x] Every current table and figure has a source-data file or documented regeneration path.
- [x] Failed and non-converged calculations are retained and labelled.
- [x] Code, environment, open-source datasets, and VASP licensing boundaries are documented.
- [x] Manuscript claims are mapped to the claim-evidence matrix and limitation audit.
- [x] The manuscript has zero abstract citations, 25 cited references, and explicit cross-references to Tables 1–5, Figure 1, Equations 1–2, and Supporting Information.
- [x] The target-journal article-type, abstract, display-item, source-data, code, and Supporting Information requirements have been audited against official ACS, Nature Communications, and RSC guidance.

## Interpretation rule

The checked provenance gates support the benchmark article. They do not promote any unrelaxed structure, failed optimisation, absolute-total-energy diagnostic, or empty calculation template into a catalyst-performance result.
