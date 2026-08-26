# DFT Protocol

## Model hierarchy

The production models are periodic slabs of the three selected two-dimensional supports. Molecular ORCA calculations may be used only for isolated fragments or cluster cross-checks. Periodic slab calculations require a periodic DFT code capable of spin polarisation, slab dipoles, charged or compensated cells, density-of-states analysis, and electrochemical solvation.

## Geometry optimisation

Use spin-polarised PBE or RPBE with a documented D3(BJ) or equivalent dispersion correction. Optimise lattice parameters for the pristine support in a separate convergence study, then use a fixed in-plane cell for defect, SAC, and adsorbate comparisons. Use at least 15 Å vacuum normal to the sheet and a dipole correction where supported. Converge the plane-wave cutoff, k-point mesh, slab size, and vacuum before production calculations. Relax adsorbates, metal atoms, and support atoms unless a frozen-layer test demonstrates that constrained layers do not alter the ranking.

A practical starting point is a 4 × 4 supercell, a 3 × 3 × 1 Monkhorst–Pack mesh for geometry optimisation, a denser mesh for final single points, and a force threshold of 0.03 eV Å⁻¹ or tighter. These are starting values, not universal defaults; convergence evidence must be archived.

## Spin and charge

Run unrestricted calculations for Fe, Co, Ni, and any structure with non-zero spin density. Enumerate plausible initial magnetic moments and retain the lowest converged state only after checking for near-degenerate alternatives. Charged nitrate calculations must state the charge-compensation method, electrostatic correction, and reference convention. Do not compare charged and neutral adsorption energies without a consistent thermodynamic cycle.

## Energetics

For a neutral, consistently referenced adsorption process, use:

\[
E_{ads}=E_{SAC+X}-E_{SAC}-E_X.
\]

Report whether the reference is a gas-phase species, aqueous species, or CHE-derived chemical potential. Add zero-point and thermal contributions only when vibrational calculations or a documented approximation support them. Apply basis-set superposition error corrections only to compatible localised-basis cluster calculations; do not transfer a cluster BSSE correction to a periodic plane-wave result.

## Solvation and potential

Use an implicit aqueous solvation model for screening where the chosen code supports it, and perform explicit-water or higher-level electrochemical checks for the shortlisted pathway. CHE is used for first-pass PCET free energies with the convention:

\[
\mu(H^+ + e^-;U)=\tfrac{1}{2}G(H_2)-eU.
\]

Potential-dependent adsorption and non-PCET steps should not automatically be assigned an integer CHE slope. Where feasible, compare key states with a constant-potential or grand-canonical treatment, because nitrate adsorption and dissociation can show non-trivial potential dependence [1].

## Transition states

Use a double-ended pathway method or a constrained/relaxed scan to generate transition-state guesses. Accept a transition state only if it has exactly one relevant imaginary frequency and connectivity is confirmed by downhill paths or an IRC-equivalent check. Transition-state work is prioritised for the predicted potential-determining step and for steps whose barrier changes the candidate ranking.

## Required audits

Before accepting a result, verify SCF convergence, geometry convergence, absence of unintended atom contacts, consistent spin state, sensible charge distribution, and stable energy under a tighter numerical setting. Every result must carry a calculation identifier linked to its input, output, structure, software version, and audit record.

## Reference

[1]: https://doi.org/10.1038/s42004-025-01579-y "Sweeney, Tran, and Goldsmith, Communications Chemistry (2025)"
