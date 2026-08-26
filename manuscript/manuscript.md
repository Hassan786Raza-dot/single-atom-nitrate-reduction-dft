# A reproducible periodic-DFT benchmark for modelling nitrate electroreduction on two-dimensional single-atom sites

## Abstract

Computational screening of nitrate-reduction catalysts is attractive because atomically dispersed metal sites and two-dimensional supports provide chemically interpretable model systems. The interpretation of a screening result nevertheless depends on more than the number of candidate structures: support construction, defect chemistry, magnetic state, cell size, vacuum, numerical cut-off, k-point sampling, charged nitrate, solvation, potential dependence, and raw-output provenance can all affect the conclusion [1–5]. Here we report an auditable benchmark workflow designed to identify which parts of a proposed 30-model single-atom-catalyst screen are structurally valid, numerically tested, electronically executed, and scientifically interpretable. The workflow uses ASE and open-source GPAW 24.1.0 for executed diagnostics, while retaining VASP-compatible input-generation policies without distributing proprietary VASP software or potentials. It generated 36 support, defect, and bare-SAC starting structures and 60 nitrate/hydrogen starting structures. All 96 starting inputs passed the defined cell, vacuum, contact, and file-integrity checks after correction of support-construction errors. An eleven-calculation compact graphene benchmark showed energy ranges of 53.484778 eV across the tested cut-offs, 8.581476 eV across k-point meshes, 0.292652 eV across vacuum heights, and 0.000000 eV between the two tested closed-shell spin settings. These are total-energy diagnostics, not adsorption-energy errors. A periodic GPAW smoke calculation completed, whereas two coarse plane-wave Fe-SAC optimisations did not satisfy the declared diagnostic force criterion. The resulting evidence supports a reproducibility benchmark and production-readiness framework, but not a catalyst ranking, nitrate adsorption dataset, free-energy pathway, transition-state catalogue, or selectivity claim. The project demonstrates why structural validity, numerical validity, electrochemical validity, and provenance must be reported as separate gates before a high-throughput nitrate-SAC screen can support mechanistic or materials-design conclusions.

**Keywords:** nitrate electroreduction; single-atom catalysts; two-dimensional materials; periodic DFT; GPAW; VASP-compatible workflow; computational hydrogen electrode; reproducibility

## 1. Introduction

Electrochemical nitrate reduction has a dual motivation: nitrate is a widespread contaminant in water and wastewater, while ammonia is an important chemical feedstock and a potential energy carrier [1,2]. Converting nitrate into ammonia can therefore couple remediation with nitrogen recovery. The proposal is appealing but chemically demanding. Nitrate-to-ammonia conversion is an eight-electron process with several possible surface intermediates, including nitrate, nitrite, nitric oxide, hydrogenated nitrogen–oxygen species, nitrogen, hydroxylamine-like species, and ammonia [1,3]. The observed product distribution depends on adsorption, proton-coupled electron transfer, N–O bond cleavage, hydrogen evolution, surface coverage, pH, electrode potential, and the stability of the active site.

Single-atom catalysts (SACs) are useful model systems because the metal centre is separated from neighbouring metal ensembles and can be stabilised by a defined coordination environment. This atomic isolation has been associated with changes in activity and selectivity in several electrocatalytic reactions [6–9]. For nitrate reduction, isolated sites are mechanistically interesting because the absence of a neighbouring metal ensemble may disfavor some N–N coupling routes, while the support and coordinating atoms can tune nitrate and hydrogen binding [1,3]. Two-dimensional materials add a second design variable: a metal can be anchored to nitrogenated carbon, a chalcogen vacancy, or a nitrogen-rich framework. These environments should not be treated as interchangeable, because they differ in stoichiometry, defect formation, local symmetry, electronic structure, and propensity for reconstruction.

The literature also shows why a single adsorption descriptor is insufficient. DFT and microkinetic studies of nitrate reduction have related oxygen and nitrogen adsorption to activity and selectivity trends on extended transition-metal surfaces, but the result depends on the elementary-step network and coverage model [4,5]. Experimental and theoretical studies of atomically dispersed M–N–C catalysts have highlighted the role of nitrate-to-nitrite and nitrite-to-ammonia cascades rather than a single overall adsorption event [3]. Active hydrogen can influence both the supply of hydrogen equivalents and the competition with nitrate chemistry [2]. Consequently, a nitrate-SAC screen must evaluate at least nitrate/H competition, relevant intermediate energetics, the stability of the active site, and the dependence of the result on the electrochemical model.

The numerical problem is equally important. The computational hydrogen electrode (CHE) provides a transparent first approximation for proton–electron chemical potentials [13,14]. It does not automatically describe potential-dependent adsorption, surface charging, interfacial electric fields, or the solvation of an anionic nitrate species. Constant-potential and grand-canonical approaches can change adsorption and dissociation energetics when the electronic charge responds to the applied potential [10,11,24]. Implicit solvation can be useful, but its dielectric, cavity, ionic-strength, and charged-surface assumptions must be reported [12,15]. A calculation that uses a plausible molecule and a converged optimiser is therefore not automatically a valid aqueous electrochemical result.

This work addresses a methodological gap that is often obscured by high-throughput language. Before asking which metal is the best nitrate-reduction SAC, one must establish whether the proposed models and settings can support the comparison. We ask: **can a matched periodic-DFT workflow distinguish file-valid starting structures from numerically and electrochemically accepted results, and which gates must be passed before a SAC ranking is defensible?** We hypothesise that geometric validity and scientific validity are separable: a structure may pass a file and contact audit while remaining unsuitable for activity ranking because the numerical setup, spin state, charge treatment, solvation model, or potential dependence is unresolved.

The contribution is intentionally bounded. We provide a complete, executable and auditable benchmark package, quantify numerical sensitivity in a compact periodic model, and define a production-readiness gate for a 30-model SAC study. We do not present a catalyst ranking because the required converged adsorption and pathway calculations have not been completed. This choice follows the central principle of reproducible computational research: the strength of a conclusion cannot exceed the strength of the evidence that supports it.

## 2. Study design and evidence hierarchy

### 2.1 Matched starting-model matrix

The proposed screen contains three support families and ten metal identities. The metals span early and late transition-metal behaviour, common non-noble candidates, platinum-group references, and late noble-metal controls. The structures are labelled starting models rather than claims about unique experimentally realised phases.

| Support | Starting model | Metals | Bare SACs |
|---|---|---|---:|
| N-graphene | 4×4 sheet; reproducible N anchor | Fe, Co, Ni, Cu, Zn, Ru, Rh, Pd, Pt, Au | 10 |
| MoS₂ vacancy | 4×4 2H-MoS₂; one S vacancy | Fe, Co, Ni, Cu, Zn, Ru, Rh, Pd, Pt, Au | 10 |
| g-C₃N₄-like | 4×4 labelled C–N model | Fe, Co, Ni, Cu, Zn, Ru, Rh, Pd, Pt, Au | 10 |
| **Total** | **Matched starting matrix** | **10 metals** | **30** |

The evidence hierarchy is explicit. Direct observations include the number and audit status of generated files, the raw convergence energies, the GPAW logs, the calculation-status ledger, and the outcomes of deterministic code tests. Derived observations include family-wise energy ranges and their pass/refine labels. Literature-supported statements concern nitrate mechanisms, SAC design, CHE, solvation, and constant-potential effects. Catalyst activity, adsorption free energies, reaction barriers, selectivity, and microkinetic rates are not evidence categories represented by the current calculations and are not reported as results.

### 2.2 Starting structures are not chemical results

The structure generator produced pristine or reference supports, defect structures where relevant, bare metal-containing structures, and nitrate/H starting geometries. A metal atom initially placed above a vacancy or anchor is not assumed to remain isolated after relaxation. It may migrate, reconstruct the defect, bind to a different coordination environment, or detach. Likewise, a nitrate geometry positioned above a metal site is not an aqueous adsorption structure. Nitrate is an anion; its charge, compensating background, solvation, electrostatic correction, and reference state must be treated together.

The final inventory contains 36 support/reference and bare-SAC inputs and 60 adsorbate inputs. A first version of the g-C₃N₄-like construction produced periodic duplicate sites because the basis translations were not scaled consistently. A second construction issue reduced the effective vacuum after adsorbate placement. Both were corrected and the complete regenerated set passed the defined starting-geometry audit. These corrections are retained in the project history rather than hidden because they demonstrate why automated structure checks are part of the scientific method.

## 3. Computational methods

### 3.1 Software and reproducibility

The executed open-source route uses GPAW 24.1.0 with ASE and the registered Ubuntu GPAW PAW datasets. The packaged GPAW extension required a NumPy 1.x-compatible isolated runtime; the exact environment and dataset location are documented in `ENVIRONMENT.md`. The project also contains VASP-compatible POSCAR, INCAR, KPOINTS, and POTCAR-manifest generation. Proprietary VASP executables and potential files are not distributed, and no VASP result is claimed.

Every accepted calculation in the planned production workflow must carry a calculation identifier, structure identifier, input files, software and dataset version, raw output, final structure, convergence summary, and audit record. The workflow distinguishes `INPUT_ONLY`, `DIAGNOSTIC_ONLY`, `ACCEPTED`, and `NOT_RUN`. This taxonomy prevents a failed or coarse calculation from being silently combined with a converged result.

### 3.2 Structural and numerical settings

The recommended production route is spin-polarised periodic DFT with a documented exchange–correlation functional, dispersion treatment, PAW dataset, slab cell, vacuum, dipole correction, k-point mesh, electronic convergence, ionic convergence, smearing, and magnetic initialisation. The in-plane cell should be converged for the pristine support and then held fixed for matched defect/SAC comparisons unless a strain study is explicitly intended. Adsorbates, the metal centre, and chemically active support atoms should be relaxed. A frozen-layer approximation is acceptable only after testing that it does not alter the observable or ranking.

For transition metals, multiple initial magnetic moments are required. A closed-shell graphene spin comparison can test a calculator path, but it cannot validate the magnetic state of Fe, Co, Ni, or other open-shell SACs. A production result should retain near-degenerate magnetic solutions and state how the selected state was chosen. Geometry convergence should be based on forces and, where relevant, stress; total-energy convergence alone is insufficient.

### 3.3 Energetics and electrochemistry

For a consistently referenced neutral adsorption process, the electronic adsorption energy is

$$
E_{ads}=E_{SAC+X}-E_{SAC}-E_X.
$$

This expression is meaningful only when the three terms share the same numerical and thermodynamic conventions. Gas-phase, aqueous, solvated-ion, and CHE-derived references must not be mixed. Zero-point and thermal corrections require vibrational calculations or a documented approximation. A cluster BSSE correction must not be transferred to a periodic plane-wave result.

For a proton–electron pair, the project uses the CHE convention

$$
\mu(H^+ + e^-;U)=\tfrac{1}{2}G(H_2)-eU,
$$

with U referenced consistently to the chosen hydrogen-electrode convention. CHE is a first-pass treatment of PCET steps. It does not automatically assign an integer potential slope to nitrate adsorption or dissociation, and it does not replace charged-surface or constant-potential calculations.

The reaction network for a future production study must include nitrate-to-nitrite chemistry, nitrite-to-ammonia chemistry, competing hydrogen evolution, alternative oxygen-removal sequences, and plausible ammonia-release steps. A transition state should have one relevant imaginary frequency and connectivity to the intended reactant and product. Solvation sensitivity should be tested for shortlisted intermediates and the potential-determining step. Stability analysis should include defect formation, metal anchoring, migration, aggregation, reconstruction, and, where relevant, dissolution.

## 4. Results

### 4.1 Structure and input audit

The final generation produced 36 bare/support structures and 60 nitrate/H starting structures. The audit checks finite cells, periodic boundary conditions, effective vacuum, minimum interatomic distance, and successful VASP-format read-back. All files passed the current geometry audit. This result establishes that the inputs are syntactically and geometrically usable; it does not establish that the structures are thermodynamically stable or experimentally realistic.

| Artefact | Number | Audit result | Meaning |
|---|---:|---|---|
| Support/reference structures | 6 | 0 failures | Valid starting cells |
| Bare SAC inputs | 30 | 0 failures | Starting configurations; not relaxed results |
| SAC + H inputs | 30 | 0 failures | Adsorption inputs; charge/spin still required |
| SAC + NO₃ inputs | 30 | 0 failures | Adsorption inputs; nitrate is charged |
| **Total** | **96** | **0 geometric failures** | **Complete traceable input inventory** |

### 4.2 Executed calculation status

A periodic graphene smoke calculation completed and generated a GPAW log, optimiser record, `.gpw` file, final geometry, and summary. This verifies that the executable route, datasets, numerical libraries, and periodic boundary conditions can operate together. It does not validate transition-metal magnetic states, charged nitrate, dispersion, implicit solvation, or production convergence.

Two coarse plane-wave Fe-SAC optimisations were attempted with a 150 eV cut-off, Gamma-only sampling, five ionic steps, and a 0.50 eV Å⁻¹ diagnostic force target. The Fe@graphene and Fe@MoS₂ plane-wave diagnostics did not meet the declared criterion. An earlier Fe@graphene LCAO diagnostic was marked converged under its own optimiser settings, but it is not merged with the plane-wave data because calculator modes and numerical settings differ.

| Run | Mode | Setting | Steps | Status |
|---|---|---|---:|---|
| Fe@graphene | LCAO | dzp-labelled; Γ | 12 | Local convergence; diagnostic only |
| Fe@graphene | Plane-wave | 150 eV; Γ | 5 | Not converged; diagnostic only |
| Fe@MoS₂ | Plane-wave | 150 eV; Γ | 5 | Not converged; diagnostic only |

### 4.3 Compact numerical benchmark

The compact benchmark used pristine graphene and varied one nominal setting at a time. The eleven calculations tested cut-offs of 150, 250, and 350 eV; 1×1×1, 2×2×1, and 3×3×1 k-point meshes; vacuum heights of 10, 15, and 20 Å; and two closed-shell spin settings. The raw values and the rounded values used in this table agree with `data/convergence/convergence.csv`.

| Family | Cases | Tested settings | Energy range (eV) | Decision |
|---|---:|---|---:|---|
| Cut-off | 3 | 150, 250, 350 eV | 53.484778 | REFINE |
| k-point | 3 | 1×1×1, 2×2×1, 3×3×1 | 8.581476 | REFINE |
| Vacuum | 3 | 10, 15, 20 Å | 0.292652 | REFINE |
| Spin | 2 | non-spin / spin-polarised | 0.000000 | PASS* |

*The spin result is a limited pass for the closed-shell graphene benchmark only.

![](figures/final/convergence_benchmark.png)

**Figure 1.** Total-energy diagnostics for the compact graphene benchmark. The three panels show the tested cut-off, k-point, and vacuum families. The figure is generated from the archived CSV and does not represent adsorption energies, activity, or a catalyst ranking. The large family-wise ranges are evidence that production settings must be refined using the actual chemical observables.

The family-wise ranges are 53.484778 eV for the cut-off series, 8.581476 eV for the k-point series, 0.292652 eV for the vacuum series, and 0.000000 eV for the two tested spin settings. Absolute total energies from different numerical settings are not themselves catalytic observables, so these ranges should not be reported as errors in nitrate adsorption. They show that a single unvalidated setting cannot be selected as a production protocol. A proper production convergence study must repeat the comparison using adsorption-energy differences, forces, geometries, magnetic moments, and reaction-step free energies for representative SAC and adsorbate systems.

## 5. Discussion

### 5.1 What has been established

The project establishes four direct findings. First, a reproducible structure generator can create a complete matched starting inventory, but automated audits are necessary because periodic translation and vacuum errors can occur even in small models. Secondly, the open-source GPAW route can execute periodic electronic-structure calculations in this environment, which establishes software feasibility but not production suitability. Thirdly, the compact benchmark shows that the numerical settings are not yet defensible for a full catalyst screen. Fourthly, the provenance taxonomy prevents diagnostic runs from being mistaken for accepted production results.

These findings address a practical problem in computational catalysis. High-throughput language can imply that every candidate has an equivalent, validated result. In reality, a candidate matrix can contain a mixture of failed relaxations, different spin states, reconstructed sites, inconsistent charge references, and non-comparable calculator modes. A valid workflow must expose those differences. The current project does so by retaining raw diagnostics and by assigning acceptance states rather than filling empty templates with guessed values.

### 5.2 What has not been established

No current calculation establishes that any of the 30 SAC models is stable under electrochemical conditions. A negative metal-binding energy relative to an isolated gas-phase atom would not alone prove resistance to aggregation, migration, dissolution, or poisoning. No current calculation establishes nitrate adsorption free energy. The nitrate inputs are charged species whose reference and compensation treatment remain to be implemented consistently. No current calculation establishes ammonia selectivity, because no complete reaction network or validated kinetic model is available. No current calculation establishes a transition-state barrier or a potential-determining step.

This boundary is scientifically important because the literature provides examples of strong nitrate-to-ammonia performance and mechanistic hypotheses, but those results cannot be transferred to a new support/metal model without reproducing the relevant structural, electronic, and electrochemical assumptions [1–5]. Similarly, a descriptor relationship developed for extended metal surfaces cannot automatically be applied to a reconstructed isolated site. The present benchmark is therefore a readiness study, not a claim that any particular metal is superior.

### 5.3 Production campaign required for a catalyst paper

A catalyst-discovery manuscript would require a second computational campaign. The pristine supports and defects must first be converged for cell, cut-off, mesh, vacuum, slab size, spin, and dispersion. All 30 bare SACs must then be relaxed with multiple magnetic initialisations and alternative starting placements. Each accepted structure should be tested for migration, aggregation, and defect reconstruction. The result should be an auditable stability table, not a list of optimiser flags.

Nitrate and H* should then be calculated with a consistent charge and thermodynamic reference. Screening should include at least nitrate-to-nitrite and nitrite-to-ammonia alternatives, competing HER, and coverage or site-blocking assumptions where relevant. Shortlisted pathways should include solvation sensitivity, CHE corrections only for appropriate PCET steps, and constant-potential or grand-canonical checks for charge-sensitive states. Transition states and thermochemical corrections should be added only where they can change the candidate ranking.

Finally, the data should support a conclusion proportionate to the model. If the study remains entirely computational, the authors should report uncertainty from numerical settings, magnetic states, structural alternatives, solvation, and reaction-network choices. If the goal is a high-impact materials claim, computational predictions should be linked to an experimentally testable synthesis and characterisation plan. A polished figure cannot compensate for missing evidence; a smaller paper with a defensible benchmark can be more valuable than a larger paper built on unvalidated rankings.

## 6. Reproducibility and data availability

The repository contains structure generators, VASP-compatible input generation, GPAW scripts, convergence analysis, plotting code, geometry audits, DOI-validation scripts, the claim-to-evidence matrix, the figure/table inventory, the production-readiness checklist, raw diagnostic records, processed status tables, the manuscript source, supporting information, and the compiled PDF. The data are separated into input structures, raw calculation artefacts, processed records, and narrative interpretation.

The minimum dataset for the present benchmark comprises the 96 starting structures, geometry-audit outputs, convergence CSV, raw GPAW diagnostic directories, run-status ledger, software environment, PAW dataset information, plotting script, and figure. A future production study should add every accepted and failed `OUTCAR`/`vasprun.xml` or equivalent GPAW archive, final geometries, charge and spin records, solvent settings, thermochemical corrections, and unique calculation identifiers. The project follows the reporting principle that readers must be able to verify the claims made in the paper; it does not imply that unexecuted calculations are available.

## 7. Conclusions

This work presents a reproducible periodic-DFT benchmark for a proposed 30-model nitrate-reduction SAC screen on two-dimensional supports. The workflow generated 36 support/reference and bare-SAC structures and 60 nitrate/H starting structures; all passed the current geometric audit. A GPAW periodic smoke calculation confirmed executable electronic-structure capability. The compact benchmark exposed family-wise total-energy sensitivity of 53.484778 eV for cut-off, 8.581476 eV for k-point mesh, and 0.292652 eV for vacuum, while the closed-shell graphene spin comparison was unchanged within the recorded precision.

The results support a clear methodological conclusion: passing a geometric audit is not equivalent to obtaining a chemically valid catalyst result. Before a nitrate-SAC ranking can be defended, the workflow must pass numerical, magnetic, charge, solvation, potential, stability, pathway, and provenance gates. The current package is therefore a complete reproducibility-stage benchmark and production-readiness framework, not a completed catalyst-discovery study. This deliberate boundary is the principal quality-control result of the work.

## References

[1] Wu Z.-Y.; Karamad M.; Yong X.; Huang Q.; Cullen D. A.; Zhu P.; Xia C.; Xiao Q.; Shakouri M.; Chen F.-Y.; Kim J. Y. T.; Xia Y.; Heck K.; Hu Y.; Wong M. S.; Li Q.; Gates I.; Siahrostami S.; Wang H. *Electrochemical ammonia synthesis via nitrate reduction on Fe single atom catalyst*. **Nature Communications** (2021). https://doi.org/10.1038/s41467-021-23115-x

[2] Fan X.; Johnson N.; et al. *Active hydrogen boosts electrochemical nitrate reduction to ammonia*. **Nature Communications** (2022). https://doi.org/10.1038/s41467-022-35664-w

[3] Murphy E.; Liu Y.; Matanovic I.; Rüscher M.; Huang Y.; Ly A.; Guo S.; Zang W.; Yan X.; Martini A.; Timoshenko J.; Roldán Cuenya B.; Zenyuk I. V.; Pan X.; Spoerke E. D.; Atanassov P. *Elucidating electrochemical nitrate and nitrite reduction over atomically-dispersed transition metal sites*. **Nature Communications** (2023). https://doi.org/10.1038/s41467-023-40174-4

[4] Liu J.-X.; Richards D.; Singh N.; Goldsmith B. R. *Activity and Selectivity Trends in Electrocatalytic Nitrate Reduction on Transition Metals*. **ACS Catalysis** (2019). https://doi.org/10.1021/acscatal.9b02179

[5] Mou T.; Wang Y.; Deák P.; Li H. *Predictive Theoretical Model for the Selective Electroreduction of Nitrate to Ammonia*. **The Journal of Physical Chemistry Letters** (2022). https://doi.org/10.1021/acs.jpclett.2c02452

[6] Subhadarshini S.; Pumera M. *Single Atom Catalyst for Nitrate-to-Ammonia Electrochemistry*. **Small** (2024). https://doi.org/10.1002/smll.202403515

[7] Yuan H.; Li Z.; Zeng X. C.; Yang J. *Descriptor-Based Design Principle for Two-Dimensional Single-Atom Catalysts: Carbon Dioxide Electroreduction*. **The Journal of Physical Chemistry Letters** (2020). https://doi.org/10.1021/acs.jpclett.0c00676

[8] Gusmão R.; et al. *Recent Developments on the Single Atom Supported at 2D Materials Beyond Graphene as Catalysts*. **ACS Catalysis** (2020). https://doi.org/10.1021/acscatal.0c02388

[9] *Surface coordination chemistry on graphene and two-dimensional carbon materials for well-defined single atom supported catalysts*. **Advances in Organometallic Chemistry** (2019). https://doi.org/10.1016/bs.adomc.2019.01.002

[10] Sweeney M.; Tran K.; Goldsmith B. R. *A grand canonical study of the potential dependence of nitrate adsorption and dissociation across metals and dilute alloys*. **Communications Chemistry** (2025). https://doi.org/10.1038/s42004-025-01579-y

[11] Van den Bossche M.; Skúlason E.; Rose-Petruck C.; Jónsson H. *Assessment of Constant-Potential Implicit Solvation Calculations of Electrochemical Energy Barriers for H₂ Evolution on Pt*. **The Journal of Physical Chemistry C** (2019). https://doi.org/10.1021/acs.jpcc.8b10046

[12] Abidin A. F. Z.; Hamada I. *Oxygen Reduction Reaction on Single-Atom Catalysts From Density Functional Theory Calculations Combined with an Implicit Solvation Model*. **The Journal of Physical Chemistry C** (2023). https://doi.org/10.1021/acs.jpcc.3c02224

[13] Nørskov J. K.; Rossmeisl J.; Logadottir A.; Lindqvist L.; Kitchin J. R.; Bligaard T.; Jónsson H. *Origin of the Overpotential for Oxygen Reduction at a Fuel-Cell Cathode*. **The Journal of Physical Chemistry B** (2004). https://doi.org/10.1021/jp047349j

[14] Nørskov J. K.; Bligaard T.; Rossmeisl J.; Christensen C. H. *Towards the computational design of solid catalysts*. **Nature Chemistry** (2009). https://doi.org/10.1038/nchem.121

[15] García-Ratés M.; López N. *Multigrid-Based Methodology for Implicit Solvation Models in Periodic DFT*. **Journal of Chemical Theory and Computation** (2016). https://doi.org/10.1021/acs.jctc.5b00949

[16] Priyadarsini A.; Kattel S. *New Insights into the Electrochemical Nitrate Reduction Reaction on Cu(111) from Theoretical Calculations*. **The Journal of Physical Chemistry C** (2025). https://doi.org/10.1021/acs.jpcc.5c02461

[17] Tong X.; Zhang Z.; Fang Z.; Guo J. *PdMoCu Trimetallenes for Nitrate Electroreduction to Ammonia*. **The Journal of Physical Chemistry C** (2023). https://doi.org/10.1021/acs.jpcc.3c00785

[18] Jia Y.; Ji Y.-G.; Xue Q.; Li F.-M. *Efficient Nitrate-to-Ammonia Electroreduction at Cobalt Phosphide Nanoshuttles*. **ACS Applied Materials & Interfaces** (2021). https://doi.org/10.1021/acsami.1c12512

[19] Liu M.; Mao Q.; Shi K.; Wang Z. *Electroreduction of Nitrate to Ammonia on Palladium–Cobalt–Oxygen Nanowire Arrays*. **ACS Applied Materials & Interfaces** (2022). https://doi.org/10.1021/acsami.1c19412

[20] Zhang G.; Wang G.; Wan Y.; Liu X. *Ampere-Level Nitrate Electroreduction to Ammonia over Monodispersed Bi-Doped FeS₂*. **ACS Nano** (2023). https://doi.org/10.1021/acsnano.3c05946

[21] Zhou X.; Xu W.; Liang Y.; Jiang H. *Dynamically Restructuring Nanoporous Cu–Co Electrocatalyst for Efficient Nitrate Electroreduction to Ammonia*. **ACS Catalysis** (2024). https://doi.org/10.1021/acscatal.4c03336

[22] Yin H.; Peng Y.; Li J. *Electrocatalytic Reduction of Nitrate to Ammonia via a Au/Cu Single Atom Alloy Catalyst*. **Environmental Science & Technology** (2023). https://doi.org/10.1021/acs.est.2c07968

[23] Long X.; Huang F.; Zhong T.; Zhao H. *One-Step Strategy to Maximize Single-Atom Catalyst Utilization in Nitrate Reduction via Bidirectional Optimization of Mass Transfer and Electron Supply*. **Environmental Science & Technology** (2025). https://doi.org/10.1021/acs.est.4c14011

[24] Liu Z.; Sun Y.-F.; Wang Y.-S.; Zhang W. *Optimal Solution for Modeling Electrocatalysis on Two-Dimensional Single-Atom Catalysts with Grand Canonical DFT*. **ACS Catalysis** (2025). https://doi.org/10.1021/acscatal.5c00199

[25] Zhang X.; et al. *Theoretical Insights into Electrocatalytic Reduction of Nitrates to Ammonia on g-C₂N Monolayer-Supported Single Nonmetal Atoms*. **The Journal of Physical Chemistry A** (2026). https://doi.org/10.1021/acs.jpca.5c07719
