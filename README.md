# Open Food Facts Data Quality Check Migration Prototype

## Overview

This repository contains a prototype for migrating **Open Food Facts data quality checks** from the legacy **Perl implementation** to a modern **Python-based validation framework**.

Open Food Facts maintains 200+ validation checks to ensure the quality and consistency of food product data. These checks are currently implemented in Perl (`DataQualityFood.pm`), which makes them harder to extend and integrate with modern data tools.

This prototype explores how these checks can be:

- Translated into Python  
- Structured in a modular and reusable way  
- Validated to ensure identical behavior  

This work is part of preparation for the **GSoC 2026 project: Data Quality Monitoring – LLM-Assisted Migration and Validation Suite**.

---

## Implemented Checks

### 1. `check_energy_for_input_set`

This check validates the **consistency of energy values** in nutrition data.

It verifies:

- Energy in **kcal should not exceed energy in kJ**
- kcal and kJ follow the expected conversion ratio  
- Detection of **reversed values**  
- Maximum energy threshold for **100g / 100ml**

**Example rule:**

> 1 kcal ≈ 4.184 kJ

**Generated warnings:**

- `energy-value-in-kcal-greater-than-in-kj`
- `energy-value-in-kcal-and-kj-are-reversed`
- `energy-value-in-kcal-does-not-match-value-in-kj`
- `value-over-3911-energy`

---

### 2. `check_specific_nutrients_for_input_set` (Partial)

This check validates **cross-nutrient consistency**.

Currently implemented rule:

- **Saturated fat should not exceed total fat**

**Example:**

- fat = 10g, saturated fat = 5g → ✅ valid  
- fat = 5g, saturated fat = 10g → ⚠️ warning  

**Generated warning:**

- `saturated-fat-greater-than-fat`

This demonstrates a **cross-field validation pattern**, where component nutrients must not exceed their totals.

---

## Design Insight

During exploration, the data quality checks were observed to follow recurring patterns:

- **Numeric validation**  
  (e.g., kcal vs kJ consistency)

- **Cross-field validation**  
  (e.g., saturated fat ≤ fat)

- **Metadata validation**  
  (e.g., NutriScore comparison)

This prototype focuses on capturing these patterns to guide scalable migration.

---

## Prototype Structure
off-quality-check-migration/
│
├── checks/
│ ├── energy_check.py
│ ├── nutrient_check.py
│
├── demo.py
├── README.md



---

## Example Test Cases

The prototype includes simple scenarios such as:

- kcal value greater than kJ  
- correct kcal ↔ kJ ratio  
- reversed kcal and kJ values  
- unrealistic energy values  
- saturated fat exceeding total fat  

These tests help ensure that the Python implementation reproduces expected validation behavior.

---

## Source of Original Checks

Original Perl module:

- `ProductOpener::DataQualityFood.pm`

Repository:

- https://github.com/openfoodfacts/openfoodfacts-server

---

## Goal of This Prototype

This is not a full migration, but a **proof-of-concept** to:

- Understand existing validation logic  
- Identify reusable validation patterns  
- Design a scalable migration strategy  
- Validate feasibility of Python-based implementation  

---

## Future Work

- Extend migration to additional checks from `DataQualityFood.pm`  
- Cover all validation types (numeric, cross-field, metadata-based)  
- Build a **parity validation framework** (Perl vs Python)  
- Design a modular **Python validation engine**  
- Explore **LLM-assisted migration workflows** (development-only)  
- Integrate with **DuckDB** for large-scale validation  

---

## Author

**Prasun Kumar**  
Computer Science & AI Student  
RGIPT, India  

Exploring contributions to **Open Food Facts – Google Summer of Code 2026**
