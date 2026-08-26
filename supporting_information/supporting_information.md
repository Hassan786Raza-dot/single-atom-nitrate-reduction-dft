# Supporting Information

## S1. Computational environment

The open-source fallback used for the executed diagnostics is GPAW 24.1.0 with ASE, Ubuntu PAW datasets, Python 3.12, NumPy 1.26.4, and SciPy 1.11.4 in an isolated runtime. VASP-compatible input generation is provided separately, but no VASP executable or proprietary POTCAR files are included.

## S2. Model inventory

The initial structure inventory contains three support families, ten metals, 36 pristine/defect/bare-SAC structures, and 60 nitrate/hydrogen starting structures. The structures are generated deterministically by `scripts/generate_structures.py` and `scripts/generate_adsorbates.py`.

## S3. Geometry audit

The geometry audit verifies finite periodic cells, periodic boundary conditions, at least 15 Å post-adsorbate vacuum, and no atom contact below 0.7 Å. The final audit reports zero failures for both the 36 bare structures and 60 adsorbate structures.

## S4. Convergence benchmark

The convergence benchmark includes cutoff values of 150, 250, and 350 eV; 1×1×1, 2×2×1, and 3×3×1 k-point meshes; 10, 15, and 20 Å vacuum; and spin-polarised/non-spin-polarised settings. Raw GPAW output is archived under `data/convergence/`. The analysis script marks cutoff, k-point, and vacuum series for refinement.

## S5. Executed diagnostic calculations

Two coarse SAC optimisations were executed for Fe@graphene and Fe@MoS₂. Both used a 150 eV plane-wave cutoff, Gamma-only sampling, five ionic steps, and a 0.50 eV Å⁻¹ diagnostic force target. They are retained as workflow diagnostics and are not included in any activity ranking.

## S6. Data acceptance policy

A numerical result is accepted only when the relevant calculation reaches the declared convergence criteria, the structure passes geometry and spin checks, the charge and electrostatic convention are documented, and the raw output is archived. Values marked `NR`, `PENDING`, or `DIAGNOSTIC_ONLY` must not be used to support catalyst rankings.
