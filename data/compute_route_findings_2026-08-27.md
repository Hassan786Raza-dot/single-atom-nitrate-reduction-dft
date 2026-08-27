# Compute-route findings

The current sandbox exposes 6 CPUs, approximately 3.8 GiB RAM, and no local NVIDIA GPU. The GPAW environment is available and verified as GPAW 24.1.0 with ASE 3.29.0 and NumPy 1.26.4, but a representative 129-atom Fe–SAC plane-wave optimisation exceeded the practical sandbox runtime after six ionic steps.

GPAW documentation confirms that the code supports periodic PAW calculations with plane-wave, LCAO, and real-space modes and provides MPI-oriented installation and execution guidance: https://gpaw.readthedocs.io/

Official Google Cloud HPC information describes scalable CPU/GPU infrastructure, workload-optimised HPC VMs, cluster tooling, and spot instances, but use of such resources requires an external cloud account and may incur charges: https://cloud.google.com/solutions/hpc

The archived UVA Research Computing chemistry guide demonstrates the standard route for periodic DFT on a Slurm cluster using MPI tasks and lists Quantum ESPRESSO, CP2K, GPAW-related dependencies, and VASP as cluster software options. Access is institution-specific: https://archive.rc.virginia.edu/userinfo/hpc/software/chemistry/

Conclusion: no suitable external compute connector or cluster is configured in the current session. The legitimate route is to execute the prepared production launcher on a user-provided or institutionally allocated HPC system. The repository contains the 90-row campaign manifest, staged protocol, ledgers, acceptance rules, and launcher required for that hand-off. No public cloud job was submitted because that would require an authenticated account and potentially billable resource creation.
