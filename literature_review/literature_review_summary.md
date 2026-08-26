# Initial Literature Review Summary

## Scope

This initial review targets computational and experimental work relevant to nitrate-to-ammonia electroreduction, isolated metal sites, two-dimensional supports, metal–support interactions, and aqueous or potential-dependent modelling. The accompanying CSV is an auditable seed dataset rather than a claim that the full 80–120-paper corpus has already been completed. Publisher metadata and method details are recorded only where they are available from the consulted source; otherwise the field is marked `NR`.

## Scientific context

Nitrate electroreduction is attractive because it couples remediation of nitrate-containing water with ammonia production. The overall transformation in acidic or neutral notation is commonly represented as NO₃⁻ + 9H⁺ + 8e⁻ → NH₃ + 3H₂O, while the alkaline form is NO₃⁻ + 6H₂O + 8e⁻ → NH₃ + 9OH⁻ [1] [2]. The reaction is mechanistically complex, involving multiple proton-coupled electron-transfer steps and competing products such as nitrite, nitric oxide, dinitrogen, and hydroxylamine.

The Fe single-atom study by Wu and co-workers provides an important benchmark for the central hypothesis of this project: isolated sites can alter selectivity by preventing elementary steps that require neighbouring metal atoms, while still enabling sequential hydrogenation of nitrogen–oxygen intermediates [1]. Their reported mechanistic analysis identified NO* → HNO* and HNO* → N* as potential-limiting transformations. This is experimentally significant because the theoretical mechanism was coupled to a demonstrated Fe SAC, rather than being only a hypothetical screening exercise.

A complementary line of work emphasises the role of adsorbed hydrogen. Fan and co-workers reported that nitrate reduction can be promoted when the production and consumption of active hydrogen are balanced, showing that suppression of hydrogen evolution is not automatically equivalent to maximising nitrate-to-ammonia activity [2]. This cautions against treating HER solely as an undesired side reaction and motivates inclusion of H* adsorption and hydrogen-transfer energetics in the screening workflow.

Recent reviews and theoretical studies broaden the design space to nitrogen-coordinated carbon, gC₂N, h-BP, transition-metal dichalcogenides, and related two-dimensional matrices [3] [4]. They consistently indicate that four coupled criteria are required: support anchoring and resistance to aggregation, favourable but not excessive nitrate adsorption, a viable sequence of intermediate transformations, and selectivity against HER or partial nitrate reduction. A single adsorption-energy descriptor is therefore unlikely to be sufficient across chemically distinct supports.

## Methodological assessment

The initial evidence supports a hierarchical computational strategy. Geometry and electronic screening can use a relatively economical, spin-polarised GGA-level protocol with dispersion, followed by higher-accuracy single points and solvation checks for shortlisted systems. However, the project brief's proposed use of molecular ORCA settings alone is not sufficient for periodic 2D slabs: periodic plane-wave or periodic localised-orbital software is required for reliable band structures, work functions, surface dipoles, and Brillouin-zone sampling. Molecular basis-set prescriptions such as `def2-SVP` and `def2-TZVP` can be appropriate for cluster models, but must not be silently presented as a universal periodic-slab protocol.

The computational hydrogen electrode remains useful for organising proton-coupled electron-transfer free energies, but its potential dependence is an approximation. Sweeney, Tran, and Goldsmith show that grand-canonical DFT predicts potential-dependent nitrate adsorption and dissociation and can differ from canonical DFT combined with CHE [5]. The project should therefore report CHE values as a first-pass model and reserve constant-potential or grand-canonical calculations for key intermediates and the predicted potential-determining step.

Implicit solvation is valuable for screening, but nitrate is charged and its interfacial environment is strongly affected by counterions, water orientation, electric fields, and electrode charge. A dielectric continuum alone should not be treated as a complete description. At minimum, the shortlisted pathway should be checked with explicit water molecules or a more advanced electrochemical treatment, and sensitivity to the solvation model should be reported.

## Gaps and open questions

The most useful gap is not simply the absence of another metal–support combination. It is the lack of controlled comparisons in which the same metal set, coordination environment, slab size, spin protocol, thermochemical treatment, and solvent treatment are held constant across several 2D supports. This project can address that gap if it uses a strict, pre-registered workflow and does not mix cluster, slab, canonical, and constant-potential results in one ranking without labelling them.

Promising understudied comparisons include the same isolated Fe, Co, Ni, Cu, Ru, Rh, Pd, Pt, and Au atoms anchored at equivalent defect or heteroatom environments in nitrogenated carbon, 2H-MoS₂, and g-C₃N₄. The comparison should be framed as a matched model family, not as a claim that all supports possess experimentally identical anchoring sites. The key mechanistic questions are whether metal charge transfer changes nitrate binding mode, whether support polarisation alters HNO* formation, and whether the site can balance nitrogen-oxygen bond activation against HER.

Descriptors worth testing are metal–support binding energy, nitrate adsorption free energy, charge on the metal, coordination number, d-band centre where a meaningful projected density of states exists, work function, and the free-energy span of the most uphill PCET step. Correlation analysis must include uncertainty, spin-state sensitivity, and leave-one-system-out checks; a high R² from a small, correlated dataset is not sufficient evidence of a transferable descriptor.

## Recommended protocol decisions

The recommended production workflow is periodic spin-polarised PBE or RPBE with a documented dispersion correction, a converged plane-wave cutoff and k-point mesh, and slab vacuum of at least 15 Å. Shortlisted structures should receive a higher-quality functional or single-point cross-check, solvation sensitivity analysis, zero-point and thermal corrections, and CHE free-energy diagrams. Charged nitrate calculations require an explicit statement of charge compensation and electrostatic treatment. Transition-state searches should be limited to steps that control the ranking and should be validated by the presence of one reaction-coordinate imaginary frequency and confirmed connectivity between minima.

The project should not claim publication readiness until every final number can be traced to raw output, all convergence and spin checks are archived, and the strongest conclusions survive reasonable changes in slab size, solvation treatment, and potential model.

## References

[1]: https://doi.org/10.1038/s41467-021-23115-x "Wu et al., Nature Communications (2021)"
[2]: https://doi.org/10.1038/s41467-022-35664-w "Fan et al., Nature Communications (2022)"
[3]: https://doi.org/10.1002/smll.202403515 "Subhadarshini and Pumera, Small (2024)"
[4]: https://doi.org/10.1021/acs.jpclett.1c00855 "Theoretical Exploration of nitrate reduction on transition-metal-doped h-BP (2021)"
[5]: https://doi.org/10.1038/s42004-025-01579-y "Sweeney, Tran, and Goldsmith, Communications Chemistry (2025)"
