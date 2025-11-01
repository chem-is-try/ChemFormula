import pytest

from chemformula.chemformula import ChemFormulaDict, ChemFormulaDictFloat


# Tests for ChemFormulaDict
def test_chemformulardict_valid_set_get():
    cf_dict = ChemFormulaDict()
    cf_dict["C"] = 6
    assert cf_dict["C"] == 6
    # missing key returns default int 0
    assert isinstance(cf_dict["N"], int)
    assert cf_dict["N"] == 0

def test_chemformulardict_invalid_symbol_raises():
    cf_dict = ChemFormulaDict()
    with pytest.raises(ValueError):
        cf_dict["Xx"] = 1  # unknown element symbol

@pytest.mark.parametrize("bad_value", [-1, 1.5, "2"])
def test_chemformulardict_invalid_frequency_types(bad_value):
    cf_dict = ChemFormulaDict()
    with pytest.raises(ValueError):
        cf_dict["C"] = bad_value

def test_chemformulardict_init_with_invalid_mapping_raises():
    with pytest.raises(ValueError):
        ChemFormulaDict({"Xx": 1})

def test_chemformulardict_init_with_invalid_dict():
    with pytest.raises(TypeError):
        ChemFormulaDict("C6H12O6")


# Tests for ChemFormulaDictFloat
def test_chemformulardictfloat_valid_set_get_and_default():
    f = ChemFormulaDictFloat()
    f["O"] = 0.5
    assert isinstance(f["O"], float)
    assert abs(f["O"] - 0.5) < 1e-12
    # missing key returns default float 0.0
    assert isinstance(f["He"], float)
    assert f["He"] == 0.0

def test_chemformulardictfloat_accept_int_and_convert_to_float():
    cf_dict = ChemFormulaDictFloat()
    cf_dict["H"] = 2
    assert isinstance(cf_dict["H"], float)
    assert cf_dict["H"] == 2.0

def test_chemformulardictfloat_invalid_symbol_raises():
    cf_dict = ChemFormulaDictFloat()
    with pytest.raises(ValueError):
        cf_dict["Xx"] = 1.0  # unknown element symbol

def test_chemformulardictfloat_invalid_value_type_raises():
    cf_dict = ChemFormulaDictFloat()
    with pytest.raises(ValueError):
        cf_dict["O"] = "0.5"  # string not allowed

def test_chemformulardictfloat_init_with_invalid_mapping_raises():
    with pytest.raises(ValueError):
        ChemFormulaDictFloat({"Xx": 1.0})

def test_chemformulardictfloat_init_with_invalid_dict():
    with pytest.raises(TypeError):
        ChemFormulaDictFloat("C6H12O6")
