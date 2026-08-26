import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from ase import Atoms
from ase.io import write
from generate_vasp_inputs import generate


def test_generate(tmp_path):
    source = tmp_path / "h2.traj"
    atoms = Atoms("H2", positions=[[0, 0, 0], [0, 0, 0.74]], cell=[8, 8, 12], pbc=True)
    write(source, atoms, format="traj")
    out = generate(str(source), str(tmp_path / "vasp"), "H2 test", 400, (2, 2, 1))
    assert (out / "POSCAR").exists()
    assert "ENCUT = 400" in (out / "INCAR").read_text()
    assert "2 2 1" in (out / "KPOINTS").read_text()
    assert "H:" in (out / "POTCAR.MANIFEST").read_text()


if __name__ == "__main__":
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        test_generate(Path(d))
    print("VASP input generator test passed")
