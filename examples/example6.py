from chemformula import ChemFormula

conjugated_diene = ChemFormula("C4H6")
dienophile = ChemFormula("C2H4")

diels_alder_adduct = conjugated_diene + dienophile

print("\n--- Adding ChemFormula Objects ---")
print(f" Butadiene {conjugated_diene.unicode} and ethylene {dienophile.unicode}"
      f" undergo a Diels-Alder reaction to form {diels_alder_adduct.unicode}.")
print(f" Molecular weight: {diels_alder_adduct.formula_weight:.2f} g/mol.")

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
print(f" Vinyl chloride {vinyl_chloride.hill_formula.unicode} is synthesized from dichloroethane"
      f" {dichloroethane.hill_formula.unicode} by elimination of hydrogen chloride"
      f" {hydrogen_chloride.hill_formula.unicode}.")
print(f" Molecular weight: {vinyl_chloride.formula_weight:.2f} g/mol.")

# OUTPUT:
#
# --- Subtracting ChemFormula Objects ---
#  Vinyl chloride C₂H₃Cl is synthesized from dichloroethane C₂H₄Cl₂ by elimination of hydrogen chloride ClH.
#  Molecular weight: 62.50 g/mol.
#


borane = ChemFormula("BH3")
diborane = 2 * borane
print("\n--- Multiplying ChemFormula Objects ---")
print(f" Diborane {diborane.hill_formula.unicode} is formed by the dimerization of two borane"
      f" {borane.hill_formula.unicode} molecules.")
print(f" Molecular weight of diborane: {diborane.formula_weight:.2f} g/mol.")

# OUTPUT:
#
# --- Multiplying ChemFormula Objects ---
#  Diborane B₂H₆ is formed by the dimerization of two borane BH₃ molecules.
#  Molecular weight of diborane: 27.67 g/mol.
#


ATP = ChemFormula("C10H12N5O13P3", -4)
water = ChemFormula("H2O")
dihydrogen_phosphate = ChemFormula("H2PO4", -1)

AMP = ATP + 2 * water - 2 * dihydrogen_phosphate

print("\n--- Arithmetics with ChemFormula Objects ---")
print(f" ATP ({ATP.hill_formula.unicode}) hydrolyzes with two water molecules"
      f" to AMP ({AMP.hill_formula.unicode}) and two inorganic phosphates ({dihydrogen_phosphate.unicode})"
      f" releasing energy for cellular processes.\n")

# OUTPUT:
#
# --- Arithmetics with ChemFormula Objects ---
#  ATP (C₁₀H₁₂N₅O₁₃P₃⁴⁻) hydrolyzes to AMP (C₁₀H₁₂N₅O₇P²⁻) and two inorganic phosphates (H₂PO₄⁻) releasing energy for cellular processes.
#
