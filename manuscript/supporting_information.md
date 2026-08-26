# Supporting Information

## Reproducibility-stage periodic-DFT benchmark for a proposed 30-model SAC nitrate-reduction screen

### S1. Scope and evidence boundary

This Supporting Information accompanies a reproducibility-stage benchmark and production-readiness framework. It does not contain an accepted catalyst ranking, nitrate adsorption-energy dataset, complete free-energy pathway, transition-state catalogue, selectivity prediction, or limiting-potential result. All such quantities remain calculation-blocked and are listed as future production gates.

### S2. Repository and environment

The complete project is archived at [GitHub](https://github.com/hassanraza147/single-atom-nitrate-reduction-dft). The executed open-source route uses GPAW 24.1.0, ASE 3.29.0, Python 3.12, NumPy 1.26.4, and the Ubuntu GPAW PAW datasets. The self-configuring GPAW scripts default to `/usr/share/gpaw-setups` when `GPAW_SETUP_PATH` is not set. VASP-compatible input generation is included, but no VASP executable or proprietary potential files are distributed and no VASP result is claimed.

### S3. Structure inventory

The proposed design contains three support families—nitrogenated graphene, a 2H-MoS₂ sulphur-vacancy model, and a labelled g-C₃N₄-like model—with ten metals each: Fe, Co, Ni, Cu, Zn, Ru, Rh, Pd, Pt, and Au. The repository contains 36 support/reference and bare-SAC starting structures and 60 nitrate/H starting structures. The machine-readable production manifest is `data/production_campaign_manifest.csv`, containing 30 `bare_SAC_optimisation` rows and 60 `adsorbate_screening` rows.

### S4. Geometry audits

The geometry audit checks file read-back, finite cell information, periodic boundary conditions, effective vacuum, minimum interatomic separations, and starting contacts. All 96 current inputs pass the defined input-level audit. This result verifies starting-file usability only. It does not establish relaxed stability, resistance to reconstruction, metal isolation under reaction conditions, or aqueous adsorption.

### S5. Numerical benchmark

The compact convergence matrix contains eleven graphene diagnostic calculations spanning cut-off, k-point mesh, vacuum, and closed-shell spin settings. It reports absolute total-energy ranges of 53.484778 eV for cut-off, 8.581476 eV for k-point mesh, 0.292652 eV for vacuum, and 0.000000 eV between the tested closed-shell spin settings. These values are diagnostics and must not be interpreted as adsorption-energy uncertainties or SAC-ranking evidence.

Production convergence must instead use adsorption-energy differences, forces, relaxed geometries, magnetic moments, and free-energy steps for representative supports, defects, SACs, and adsorbates.

### S6. Calculation-status taxonomy

Each calculation is assigned one of the following statuses:

| Status | Meaning |
|---|---|
| `INPUT_ONLY` | Input structure exists but no electronic-structure result is accepted. |
| `DIAGNOSTIC_ONLY` | A calculation ran or partially ran but does not satisfy the declared production criteria. |
| `ACCEPTED` | All declared convergence, geometry, spin, provenance, and method checks pass. |
| `NOT_RUN` | Required calculation has not been executed. |

Failed calculations and partial outputs are retained. The interrupted Fe@graphene representative run is archived under `data/gpaw_production/Fe_graphene_PW250/` and is explicitly labelled diagnostic-only.

### S7. Production campaign

The staged protocol is documented in `PRODUCTION_CAMPAIGN.md`. It requires support/defect convergence, 30 bare-SAC optimisations with multiple spin states and alternative placements, nitrate/H* screening with declared charge treatment, complete nitrate-to-ammonia and HER networks, transition-state verification where ranking-relevant, solvation and potential sensitivity, stability analysis, uncertainty propagation, and experiment-facing validation where a materials claim is intended.

### S8. Reproduction commands

From a clean checkout, the deterministic validation suite can be run with:

```bash
/usr/bin/python3 scripts/run_validation_suite.py
```

The periodic GPAW smoke test can be run with:

```bash
.venv-gpaw/bin/python scripts/run_gpaw_smoketest.py
```

A production optimisation is executed only as an explicitly labelled campaign task, for example:

```bash
.venv-gpaw/bin/python scripts/run_gpaw_sac.py \
  structures/initial/ase_generated/graphene_N4/Fe@graphene_N4.vasp \
  data/gpaw_production/Fe_graphene_PW350 \
  --cutoff 350 --kmesh 3 3 1 --fmax 0.03 --steps 200
```

This command is a template and its output must pass the acceptance rules before entering a chemical dataset.

### S9. Final limitations

The current evidence does not establish electrochemical stability, nitrate adsorption free energies, potential-dependent energetics, solvation effects, reaction barriers, ammonia selectivity, HER competition, limiting potentials, microkinetic rates, or a best SAC. These omissions are scientific boundaries rather than formatting defects. The benchmark contribution is the explicit separation of structural, numerical, electrochemical, stability, pathway, uncertainty, and provenance gates.
