# Table S1. Compact periodic-DTF convergence benchmark

The table reports total energies from the compact pristine-graphene benchmark. Because these are absolute total energies, the values are diagnostic only; production acceptance must be based on converged energy differences for the actual slab and adsorbate systems.

| Test family | Setting | Cutoff (eV) | k-mesh | Vacuum (Å) | Spin-polarised | Total energy (eV) | QC status |
|---|---:|---:|---|---:|---|---:|---|
| Cutoff | 150 | 150 | 1×1×1 | 12 | No | -9.954667 | REFINE |
| Cutoff | 250 | 250 | 1×1×1 | 12 | No | -52.554961 | REFINE |
| Cutoff | 350 | 350 | 1×1×1 | 12 | No | -63.439445 | REFINE |
| k-point mesh | 1×1×1 | 250 | 1×1×1 | 12 | No | -52.554961 | REFINE |
| k-point mesh | 2×2×1 | 250 | 2×2×1 | 12 | No | -61.136437 | REFINE |
| k-point mesh | 3×3×1 | 250 | 3×3×1 | 12 | No | -60.934674 | REFINE |
| Vacuum | 10 | 250 | 1×1×1 | 10 | No | -52.091381 | REFINE |
| Vacuum | 15 | 250 | 1×1×1 | 15 | No | -52.384033 | REFINE |
| Vacuum | 20 | 250 | 1×1×1 | 20 | No | -52.130281 | REFINE |
| Spin | False | 250 | 1×1×1 | 15 | No | -52.384033 | PASS |
| Spin | True | 250 | 1×1×1 | 15 | Yes | -52.384033 | PASS |

**Interpretation.** The large cutoff, k-point, and vacuum sensitivities prevent these settings from being promoted to a production protocol. The spin comparison is stable for this closed-shell graphene benchmark but does not validate open-shell transition-metal SACs.
