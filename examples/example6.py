from chemformula import ChemFormula

conjugated_diene = ChemFormula("C4H6")
dienophile = ChemFormula("C2H4")

diels_alder_adduct = conjugated_diene + dienophile

print("\n--- Adding ChemFormula Objects ---")
print(f" Butadiene {conjugated_diene.unicode} and ethylene {dienophile.unicode} undergo a Diels-Alder reaction to form {diels_alder_adduct.unicode}.")  # noqa: E501
print(f" Molecular weight: {diels_alder_adduct.formula_weight:.2f} g/mol.\n")  # noqa: E501

# OUTPUT:
#
# --- Adding ChemFormula Objects ---
#  Butadiene C₄H₆ and ethylene C₂H₄ undergo a Diels-Alder reaction to form C₆H₁₀.
#  Molecular weight: 82.15 g/mol.
#
