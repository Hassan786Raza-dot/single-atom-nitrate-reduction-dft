# Production evidence ledgers

These ledgers define the minimum records required before any catalyst-discovery claim can enter the manuscript. Blank or `NOT_RUN` entries are not scientific results.

## 1. Adsorption and electrochemical ledger

Required columns:

```text
record_type,calculation_id,sac_id,support,metal,adsorbate,total_charge,background_convention,dipole_correction,solvation_model,potential_V,reference_state,E_complex,E_sac,E_reference,E_ads,ZPE,thermal,solvation_correction,G_ads,spin_state,force_max,scf_converged,ionic_converged,audit_status
```

Acceptance requires chemically consistent references, declared charge treatment, converged electronic and ionic states, geometry/contact checks, spin validation, and a complete raw-output archive.

## 2. Reaction and transition-state ledger

Required columns:

```text
record_type,calculation_id,sac_id,step,initial_state,final_state,proton_electron_pairs,potential_V,delta_E,ZPE,thermal,solvation,delta_G,barrier,imaginary_modes,connectivity_verified,HER_comparison,PDS_flag,audit_status
```

A barrier is accepted only when the transition state has the intended imaginary mode, verified connectivity, and complete frequency/output records. A limiting potential is accepted only after all competing pathway steps are present under matched conventions.

## 3. Stability ledger

Required columns:

```text
record_type,calculation_id,sac_id,alternative_structure,metal_binding_reference,defect_reference,migration_metric,aggregation_metric,reconstruction_metric,dissolution_metric,poisoning_state,minimum_stability_metric,conditions,raw_archive,audit_status
```

A stable-site label requires defined reference states and comparison of chemically plausible alternatives. A negative single-atom binding energy alone is insufficient.

## 4. Sensitivity and uncertainty ledger

Required columns:

```text
sac_id,observable,baseline_value,cutoff_delta,kmesh_delta,vacuum_delta,slab_delta,spin_delta,structure_delta,solvation_delta,potential_delta,thermochemistry_delta,pathway_delta,combined_uncertainty,rank_interval,rank_stable,audit_status
```

Report sensitivity ranges and rank intervals rather than a single deterministic ranking when perturbations change the result. Do not populate this ledger with assumed or simulated values.

## 5. Experimental validation plan

For any shortlisted SAC, record a synthesis route, metal loading, support and defect preparation, microscopy/elemental mapping, X-ray absorption or suitable coordination analysis, oxidation-state analysis, electrochemical cell and reference electrode, nitrate concentration, pH, potential range, ammonia quantification method, nitrate/nitrite mass balance, isotope-control plan where available, blank support control, metal-free control, homogeneous-metal control, and post-reaction leaching measurement.

## 6. Evidence rule

A manuscript claim may be promoted from `NOT_RUN` or `DIAGNOSTIC_ONLY` to `ACCEPTED` only when the ledger row points to a unique calculation identifier, complete raw outputs, final structure, method metadata, convergence record, and independent audit. The production manifest and claim-evidence matrix must be updated in the same commit as any accepted result.
