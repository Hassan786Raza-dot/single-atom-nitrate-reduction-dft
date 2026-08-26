# Project Status

## Completed in the initial reproducible stage

The repository, literature seed dataset, critical synthesis, support/metal selection, periodic-DFT protocol, data conventions, deterministic chemistry utilities, unit tests, validation report, and audit log are complete and synchronised to GitHub.

## Pending prerequisites

The full 30-model SAC matrix, optimised geometries, adsorption energies, transition states, projected densities of states, Bader or Hirshfeld charges, solvation corrections, stability metrics, selectivity analysis, figures, tables, and manuscript results require executed periodic DFT calculations. Those outputs are intentionally absent until they can be generated and checked under a named software version and computational environment.

## Next executable stage

1. Install or provide access to a periodic DFT engine and establish the licence/academic-use conditions.
2. Generate and inspect pristine-support and defect geometries.
3. Converge cell, vacuum, cutoff, k-point, spin, and slab-size settings.
4. Optimise the 30 bare SAC models, preserving all raw outputs.
5. Begin nitrate/H* screening, then expand to the complete pathway for shortlisted systems.

## Quality gate

No candidate may be called a best catalyst, no limiting potential may be reported as a result, and no publication-ready manuscript may be written around numerical findings until the validation and audit gates in `validation_report.md` are passed.
