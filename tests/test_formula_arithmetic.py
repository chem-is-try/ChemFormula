import pytest

from chemformula import ChemFormula

# Tests for functionality


@pytest.mark.parametrize(
    "testinput1, testinput2, expected",
    [
        (ChemFormula("H2O", 0), ChemFormula("H", 1), ChemFormula("H3O", 1)),
        (ChemFormula("Ba", 2), ChemFormula("SO4", -2), ChemFormula("BaSO4", 0)),
        (ChemFormula("C4H6", 0), ChemFormula("C2H4", 0), ChemFormula("C6H10", 0)),
    ],
)
def test_addition(testinput1, testinput2, expected):
    assert testinput1 + testinput2 == expected


# Tests for error handling


def test_addition_failed():
    with pytest.raises(TypeError):
        ChemFormula("H2O") + "H+"
