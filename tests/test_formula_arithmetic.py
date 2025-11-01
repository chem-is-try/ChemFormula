import pytest

import chemformula.config
from chemformula.chemformula import ChemFormula

# Tests for functionality

@pytest.fixture(autouse=True, scope="module")
def enable_hydrogen_isotopes():
    chemformula.config.AllowHydrogenIsotopes = True


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


@pytest.mark.parametrize(
    "testinput1, testinput2, charge_testinput2, expected_isotope, expected_radioactive",
    [
        ("H2O", "D", 1, True, False),
        ("U", "O2", 0, False, True),
    ],
)
def test_addition_properties(testinput1, testinput2, charge_testinput2, expected_isotope, expected_radioactive):
    adduct = ChemFormula(testinput1) + ChemFormula(testinput2, charge_testinput2)
    assert adduct.contains_isotopes == expected_isotope
    assert adduct.is_radioactive == expected_radioactive


@pytest.mark.parametrize(
    "testinput1, testinput2, expected",
    [
        (ChemFormula("H3O", 1), ChemFormula("H", 1), ChemFormula("H2O", 0)),
        (ChemFormula("CH2ClCH3", 0), ChemFormula("HCl", 0), ChemFormula("CH2CH2", 0)),
    ],
)
def test_subtraction(testinput1, testinput2, expected):
    assert testinput1 - testinput2 == expected


@pytest.mark.parametrize(
    "testinput1, testinput2, expected",
    [
        (ChemFormula("C2H4", 0), 2, ChemFormula("C4H8", 0)),
        (2, ChemFormula("C2H4", 0), ChemFormula("C4H8", 0)),
        (ChemFormula("Na", 1), 4, ChemFormula("Na4", 4)),
    ],
)
def test_multiplication(testinput1, testinput2, expected):
    assert testinput1 * testinput2 == expected


# Tests for error handling


def test_addition_failed():
    with pytest.raises(TypeError):
        ChemFormula("H2O") + "H+"


def test_subtraction_failed_type():
    with pytest.raises(TypeError):
        ChemFormula("H2O") - "H+"


def test_subtraction_failed_negative_frequency():
    with pytest.raises(ValueError):
        ChemFormula("H2O") - ChemFormula("H3")


def test_subtraction_failed_empty_formula():
    with pytest.raises(ValueError):
        ChemFormula("H2O") - ChemFormula("OH2")


def test_multiplication_failed():
    with pytest.raises(TypeError):
        ChemFormula("C2H4") * 0.5
    with pytest.raises(TypeError):
        0.5 * ChemFormula("C2H4")
    with pytest.raises(TypeError):
        ChemFormula("C2H4") * "2"
    with pytest.raises(TypeError):
        "2" * ChemFormula("C2H4")
    with pytest.raises(TypeError):
        ChemFormula("C2H4") * ChemFormula("H2")


def test_multiplication_failed_non_positive_integer():
    with pytest.raises(ValueError):
        ChemFormula("C2H4") * -2
    with pytest.raises(ValueError):
        ChemFormula("C2H4") * 0
