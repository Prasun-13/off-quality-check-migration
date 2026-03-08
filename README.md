# Open Food Facts Data Quality Check Migration Prototype

## Overview
This repository contains a prototype for migrating **Open Food Facts data quality checks** from the legacy **Perl implementation** to a **Python-based validation framework**.

The goal of this prototype is to explore how existing checks from the Open Food Facts backend can be translated into Python while preserving the same validation logic and warnings.

This work is part of an experimental prototype for the **GSoC project: Data Quality Monitoring – LLM-Assisted Migration and Validation Suite**.

---

## Implemented Check

### check_energy_for_input_set

This check validates the **consistency of energy values** in nutrition data.

It verifies:

1. Energy in **kcal should not be greater than energy in kJ**
2. Energy values in kcal and kJ follow the expected conversion ratio
3. Possible reversed values between kcal and kJ
4. Maximum energy threshold when nutrition values are expressed per **100g or 100ml**

Example rule:

1 kcal ≈ 4.184 kJ

Large deviations from this ratio trigger warnings.

---

## Example Warnings

The check may generate warnings such as:

- `energy-value-in-kcal-greater-than-in-kj`
- `energy-value-in-kcal-and-kj-are-reversed`
- `energy-value-in-kcal-does-not-match-value-in-kj`
- `value-over-3911-energy`

These warnings replicate the behavior of the original Perl validation logic.

---

## Source of Original Check

Original Perl module:

ProductOpener::DataQualityFood.pm

Repository:

https://github.com/openfoodfacts/openfoodfacts-server

Function migrated:

check_energy_for_input_set


---

## Prototype Structure
off-quality-check-migration/
│
├── energy_check_demo.py
└── README.md

---

## Example Test Cases

The prototype includes simple test scenarios such as:

- kcal value greater than kJ
- correct kcal ↔ kJ ratio
- reversed kcal and kJ values
- unrealistic energy density

These tests help verify that the migrated Python logic reproduces the expected warnings.

---

## Future Work

Planned extensions for the prototype include:

- Migrating additional validation checks from `DataQualityFood.pm`
- Implementing a **parity testing framework** to compare Perl and Python outputs
- Experimenting with **LLM-assisted code conversion** for automated migration
- Integrating checks into a **Python-based data quality validation engine**

---

## Author

Prasun Kumar  
CS & AI Student  
Exploring contributions to **Open Food Facts – Google Summer of Code 2026**
