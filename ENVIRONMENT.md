# Computational Environment

## Verified route

The executable route used in this repository is Ubuntu's packaged **GPAW 24.1.0** with ASE and the system PAW dataset collection. GPAW is open-source; its PAW setup files are distributed separately under the applicable GPAW data terms. VASP was not used because no licensed executable or `POTCAR` library was available.

The runtime requires NumPy 1.x and a compatible SciPy release because the packaged GPAW native extension was built against the NumPy 1.x ABI. The working environment was created as `.venv-gpaw`, which is ignored by Git.

## Reproduction setup

```bash
sudo apt-get update
sudo apt-get install -y gpaw gpaw-data python3.12-venv
/usr/bin/python3 -m venv --system-site-packages .venv-gpaw
.venv-gpaw/bin/pip install 'numpy<2' 'scipy<1.12'
export GPAW_SETUP_PATH=/usr/share/gpaw-setups:$HOME/gpaw-data/gpaw-basis-NAO-sz+coopt-NGTO-0.9.11271
```

The GPAW PAW dataset directory is already present on the working system. Network retrieval of the official setup package returned HTTP 403 during this session, so the preinstalled Ubuntu dataset was used. The dataset path, GPAW version, Python version, NumPy/SciPy versions, and calculation logs must be recorded for any result intended for publication.

## Validation status

A periodic graphene smoke test completed successfully. A Fe@graphene coarse plane-wave run completed five ionic steps but did not meet the requested final force threshold and is therefore not an accepted optimised structure. The initial LCAO and plane-wave results are retained as diagnostics only; they must not be combined into one quantitative dataset.

## Important limitation

GPAW is a valid open-source periodic DFT engine, but a minimal-basis or low-cutoff coarse run is not automatically equivalent to a converged VASP/PBE-D3 production calculation. The project must report the actual engine, settings, PAW data, convergence evidence, and residual uncertainty rather than describing GPAW results as VASP results.
