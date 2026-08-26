# Supporting Information

## S1. Purpose and scope

This Supporting Information documents the reproducible benchmark accompanying the manuscript. It describes the computational environment, structure-generation rules, geometry checks, convergence data, executed diagnostic runs, provenance taxonomy, citation audit, and production-readiness gates. It does not contain unexecuted adsorption energies, transition-state barriers, free-energy pathways, catalyst rankings, or selectivity values.

## S2. Software and licensing

The executed open-source route uses GPAW 24.1.0 with ASE in an isolated Python environment. The project records the Python, NumPy, and SciPy versions and the registered Ubuntu GPAW PAW dataset path in `ENVIRONMENT.md`. GPAW is used under its open-source licence. VASP-compatible POSCAR, INCAR, KPOINTS, and POTCAR-manifest generation is provided for future licensed calculations; proprietary VASP executables and PAW potentials are not redistributed.

## S3. Structure generation

The structure generator creates three support families: nitrogenated graphene, 2H-MoS₂ with one sulphur vacancy, and a labelled g-C₃N₄-like carbon–nitrogen starting model. Ten metals are placed at the defined anchor or vacancy environment: Fe, Co, Ni, Cu, Zn, Ru, Rh, Pd, Pt, and Au. This produces 30 bare SAC starting configurations. The adsorbate generator adds labelled H and NO₃ starting geometries to each bare model, producing 60 adsorbate inputs.

The structures are not assumed to be relaxed, stable, isolated after optimisation, or representative of every experimental polymorph. Metal migration, reconstruction, aggregation, dissolution, and alternative coordination are future chemical checks, not outcomes of the starting-geometry generator.

## S4. Geometry audit

The geometry audit reads every structure through a direct VASP-format parser and checks that the cell is finite, periodic boundary conditions are present, effective vacuum is at least 15 Å after adsorbate placement, and no interatomic distance is below 0.7 Å. The final records are `data/geometry_audit.txt` and `data/adsorbate_geometry_audit.txt`. They report 36 checked bare/support structures with zero failures and 60 checked adsorbate structures with zero failures.

Passing this audit means that the files satisfy the defined input-level checks. It does not establish energy minimisation, thermodynamic stability, a valid aqueous nitrate reference, or catalytic activity.

## S5. Numerical benchmark

The compact benchmark uses a pristine graphene model and varies cut-off, k-point mesh, vacuum height, and closed-shell spin treatment. The complete source table is `data/convergence/convergence.csv`, and family-wise analysis is produced by `scripts/analyse_convergence.py`. The benchmark contains 11 calculations after the header: three cut-off values, three k-point meshes, three vacuum heights, and two spin settings.

The family-wise total-energy ranges are 53.484778 eV for cut-off, 8.581476 eV for k-point mesh, 0.292652 eV for vacuum, and 0.000000 eV for spin. These are total-energy diagnostics. They are not adsorption-energy uncertainties and cannot be used to rank catalysts. Production convergence must compare the same chemical observable, including adsorption-energy differences, forces, geometries, magnetic moments, or reaction-step free energies.

## S6. Executed calculation-status records

A periodic graphene smoke calculation completed and produced a GPAW log, optimiser record, `.gpw` archive, final geometry, and summary. Two coarse plane-wave Fe-SAC optimisations were attempted using a 150 eV cut-off, Gamma-only sampling, five ionic steps, and a 0.50 eV Å⁻¹ diagnostic force target. Fe@graphene and Fe@MoS₂ did not meet that criterion. An earlier Fe@graphene LCAO diagnostic was marked converged under its local criterion but is not comparable to the plane-wave diagnostics.

These records are parsed into `data/parsed_run_status.csv`. The acceptance field is deliberately conservative: a local optimiser flag does not automatically promote a run to an accepted production result.

## S7. Electrochemical conventions

For a neutral consistently referenced process, the electronic adsorption energy is `E_ads = E_SAC+X − E_SAC − E_X`. The reference state must be identified as gas-phase, aqueous, solvated, or CHE-derived. Nitrate is charged, so its calculation requires a documented cell-charge and electrostatic convention, solvation treatment, and thermodynamic reference. The CHE relation `μ(H+ + e−; U) = 1/2 G(H₂) − eU` is used only as a first-pass convention for appropriate proton–electron-transfer steps.

No nitrate adsorption free energies or pathway free energies are included in the present benchmark. A future production calculation must validate charged nitrate and potential-sensitive states with a consistent electrochemical model.

## S8. Data and provenance taxonomy

The project uses four status classes. `INPUT_ONLY` means a generated starting structure with no accepted calculation. `DIAGNOSTIC_ONLY` means an executed run that is useful for testing but does not meet production criteria. `ACCEPTED` means a calculation that meets the declared numerical, structural, electronic, and provenance gates. `NOT_RUN` means that the requested calculation has not been executed. Empty cells must not be interpreted as zero.

The claim-to-evidence matrix is stored in `claim_evidence_matrix.csv`. It prohibits catalyst-ranking, adsorption-energy, transition-state, pathway, and selectivity claims unless the necessary data exist.

## S9. Figure and table provenance

The convergence figure is generated by `scripts/plot_convergence.py` from `data/convergence/convergence.csv`. The figure is embedded in the main manuscript and labelled as a diagnostic. The figure/table inventory in `figure_table_inventory.md` lists the source data and status of every current and planned visual element. Planned stability, descriptor, free-energy, and microkinetic figures are not generated because their source calculations do not exist.

## S10. Reproduction commands

From the repository root, the structure workflow is run with `python3 scripts/generate_structures.py` and `python3 scripts/generate_adsorbates.py`; audits are run with `python3 scripts/audit_geometries.py`; convergence analysis is run with `python3 scripts/analyse_convergence.py`; and the final audit is run with `python3 scripts/final_audit.py`. The standalone tests are run directly with `python3 scripts/tests/test_chemistry_utils.py` and `python3 scripts/tests/test_vasp_inputs.py`. A full pytest installation is not assumed.

## S11. Production-readiness gate

The complete checklist is stored in `production_readiness_checklist.md`. Before a catalyst-ranking article is attempted, the study must pass structure/stability, numerical, electrochemical, mechanism/selectivity, provenance, and publication gates. In particular, nitrate charge and solvation, competing HER, alternative nitrate/nitrite pathways, magnetic states, transition-state connectivity, and uncertainty from numerical settings must be resolved.
