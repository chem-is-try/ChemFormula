from chemformula import ChemFormula

conjugated_diene = ChemFormula("C4H6")
dienophile = ChemFormula("C2H4")

diels_alder_adduct = conjugated_diene + dienophile

print("\n--- Adding ChemFormula Objects ---")
print(f" Butadiene {conjugated_diene.unicode} and ethylene {dienophile.unicode} undergo a Diels-Alder reaction to form {diels_alder_adduct.unicode}.")  # noqa: E501
print(f" Molecular weight: {diels_alder_adduct.formula_weight:.2f} g/mol.")  # noqa: E501

# OUTPUT:
#
# --- Adding ChemFormula Objects ---
#  Butadiene C₄H₆ and ethylene C₂H₄ undergo a Diels-Alder reaction to form C₆H₁₀.
#  Molecular weight: 82.15 g/mol.
#

dichloroethane = ChemFormula("ClH2CCH2Cl")
hydrogen_chloride = ChemFormula("HCl")
vinyl_chloride = dichloroethane - hydrogen_chloride

print("\n--- Subtracting ChemFormula Objects ---")
print(f" Vinyl chloride {vinyl_chloride.hill_formula.unicode} is synthesized from dichloroethane {dichloroethane.hill_formula.unicode} by elimination of hydrogen chloride {hydrogen_chloride.hill_formula.unicode}.")  # noqa: E501
print(f" Molecular weight: {vinyl_chloride.formula_weight:.2f} g/mol.")  # noqa: E501

# OUTPUT:
#
# --- Subtracting ChemFormula Objects ---
#  Vinyl chloride C₂H₃Cl is synthesized from dichloroethane C₂H₄Cl₂ by elimination of hydrogen chloride ClH.
#  Molecular weight: 62.50 g/mol.
#

ATP = ChemFormula("C10H12N5O13P3", -4)
water = ChemFormula("H2O")
dihydrogen_phosphate = ChemFormula("H2PO4", -1)

ADP = ATP + water - dihydrogen_phosphate

print("\n--- Arithmetics with ChemFormula Objects ---")
print(f" ATP {ATP.hill_formula.unicode} hydrolyzes to ADP {ADP.hill_formula.unicode} and inorganic phosphate {dihydrogen_phosphate.unicode} releasing energy for cellular processes.\n")  # noqa: E501

# OUTPUT:
#
# --- Arithmetics with ChemFormula Objects ---
#  ATP C₁₀H₁₂N₅O₁₃P₃⁴⁻ hydrolyzes to ADP C₁₀H₁₂N₅O₁₀P₂³⁻ and inorganic phosphate H₂PO₄⁻ releasing energy for cellular processes.
#
