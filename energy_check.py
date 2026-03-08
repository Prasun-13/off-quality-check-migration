def check_energy_for_input_set(product, nutrition_set, set_id, data_quality_tags):
    warnings = []

    nutrients = nutrition_set.get("nutrients", {})

    energy_kj = nutrients.get("energy-kj")
    energy_kcal = nutrients.get("energy-kcal")

    # -------------------------------
    # kcal greater than kj
    # -------------------------------
    if energy_kj is not None and energy_kcal is not None:

        if energy_kcal > energy_kj:
            warnings.append(f"{set_id}-energy-value-in-kcal-greater-than-in-kj")

            if (energy_kcal > 3.7 * energy_kj - 2) and (energy_kcal < 4.7 * energy_kj + 2):
                warnings.append(f"{set_id}-energy-value-in-kcal-and-kj-are-reversed")

        # -------------------------------
        # kcal / kj mismatch
        # -------------------------------
        if (energy_kj < 3.7 * energy_kcal - 2) or (energy_kj > 4.7 * energy_kcal + 2):
            warnings.append(f"{set_id}-energy-value-in-kcal-does-not-match-value-in-kj")

    # -------------------------------
    # max energy threshold
    # -------------------------------
    per = nutrition_set.get("per")

    if per in ["100g", "100ml"]:
        if energy_kj is not None and energy_kj > 3911:
            warnings.append(f"{set_id}-value-over-3911-energy")

    return warnings

product = {}

nutrition_set = {
    "nutrients": {
        "energy-kj": 100,
        "energy-kcal": 300
    },
    "per": "100g"
}

warnings = check_energy_for_input_set(
    product,
    nutrition_set,
    "nutrition",
    "data_quality_warnings_tags"
)

print(warnings)