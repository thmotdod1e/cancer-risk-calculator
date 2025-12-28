#!/usr/bin/env python3
"""
Cancer Risk Calculator

A simple command-line tool for estimating lung cancer risk based on
smoking-related variables, with special emphasis on the age of first
cigarette consumption as a primary predictor.
"""

def calculate_risk(age, pack_years, age_first_cigarette):
    """
    Calculate lung cancer risk score.
    
    Parameters:
    age (int): Current age of the individual.
    pack_years (float): Smoking intensity (packs per day * years smoked).
    age_first_cigarette (int): Age at which the individual started smoking.
    
    Returns:
    float: Estimated risk score.
    """
    # TODO: Implement actual calculation logic.
    # Placeholder: simple linear combination.
    risk = (age * 0.1) + (pack_years * 0.5) + (age_first_cigarette * -0.2)
    return risk


if __name__ == "__main__":
    # Example usage
    risk = calculate_risk(50, 20.0, 16)
    print(f"Estimated lung cancer risk score: {risk}")
