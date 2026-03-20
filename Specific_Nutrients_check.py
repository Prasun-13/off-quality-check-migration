def check_saturated_fat(product, set_id="nutrition"):
    nutrients = product.get("nutrients", {})

    fat = nutrients.get("fat")
    sat_fat = nutrients.get("saturated-fat")

    warnings = []

    if fat is not None and sat_fat is not None:
        if sat_fat > fat:
            warnings.append(f"{set_id}-saturated-fat-greater-than-fat")

    return warnings

tests = [
    {"fat": 10, "saturated-fat": 5},   # valid
    {"fat": 5, "saturated-fat": 10},   # invalid
]

for t in tests:
    product = {"nutrients": t}
    print(check_saturated_fat(product))