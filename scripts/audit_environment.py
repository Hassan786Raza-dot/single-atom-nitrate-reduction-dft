from importlib.util import find_spec
from shutil import which

executables = ["vasp_std", "vasp_gam", "vasp_ncl", "pw.x", "cp2k", "orca", "xtb"]
packages = ["ase", "pymatgen", "numpy", "pandas", "scipy", "matplotlib"]
print("Executables")
for name in executables:
    print(f"{name}: {which(name) or 'unavailable'}")
print("Python packages")
for name in packages:
    if find_spec(name) is None:
        print(f"{name}: unavailable")
    else:
        module = __import__(name)
        print(f"{name}: {getattr(module, '__version__', 'installed')}")
