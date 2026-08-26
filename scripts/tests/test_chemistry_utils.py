import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from chemistry_utils import (ReactionStep, adsorption_energy, che_pcet_free_energy,
                             limiting_potential, write_orca_input)


def test_adsorption_energy():
    assert adsorption_energy(-12.0, -10.0, -1.5) == -0.5


def test_che_contribution():
    assert che_pcet_free_energy(2.0, 2, -0.5) == 3.0


def test_limiting_potential():
    steps = [ReactionStep("a", 0.4, 1), ReactionStep("b", 0.6, 2)]
    assert limiting_potential(steps) == -0.4


def test_orca_input():
    text = write_orca_input("H 0 0 0\nH 0 0 0.74", 0, 1)
    assert "* xyz 0 1" in text
    assert text.rstrip().endswith("*")


if __name__ == "__main__":
    test_adsorption_energy()
    test_che_contribution()
    test_limiting_potential()
    test_orca_input()
    print("All chemistry utility tests passed")
