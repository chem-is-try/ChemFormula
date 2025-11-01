# Changelog

## 1.5.1 (2025-11-01)

### New Features
- Add `+` operator to combine two ChemFormula instances by summing element counts and charges (see [example6.py](https://github.com/molshape/ChemFormula/tree/main/examples/example6.py))
- Add `-` operator to subtract one ChemFormula instance from another one by subtracting element counts and charges (see [example6.py](https://github.com/molshape/ChemFormula/tree/main/examples/example6.py))
- Add `*` operator to multiply element counts and charge with a positive integer from left and right

### Example
```python
from chemformula import ChemFormula

water = ChemFormula("H2O")
proton = ChemFormula("H", 1)

oxonium = water + proton  # => ChemFormula("H3O", 1)
hydroxonium = oxonium + 3 * water  # => ChemFormula("H9O4", 1)

print(oxonium.hill_formula.unicode)  # => H₃O⁺
print(oxonium - proton == water)  # True
print(hydroxonium.hill_formula.unicode)  # => H₉O₄⁺
```

---

## 1.5.0 (2025-09-14)

### New Feature
- Add support for hydrogen isotopes (deuterium "D" and tritium "T") via a global `AllowHydrogenIsotopes` flag in `chemformula.config` (see [example5.py](https://github.com/molshape/ChemFormula/tree/main/examples/example5.py))
- Implement `.contains_isotopes` attribute to the `ChemFormula` class for detecting specific isotopes in formulas

### Deprecated Feature
- Replace `.radioactive` property with `.is_radioactive`
- `.radioactive` can still be used, but is flagged as deprecated and emits a `DeprecationWarning`

### Example
```python
import chemformula.config
from chemformula import ChemFormula

chemformula.config.AllowHydrogenIsotopes = True

heavy_water = ChemFormula("D2O")
print(f"{heavy_water.formula_weight:.2f} g/mol")  # => 20.03 g/mol

super_heavy_water = ChemFormula("T2O")
print(super_heavy_water.is_radioactive)  # => True
```
