def calculate_risk_profile(answers: dict):
    """
    Weighted scoring for advanced risk assessment.
    answers example:
    {
        "time_horizon": 4,
        "income_stability": 3,
        "experience": 2,
        "loss_tolerance": 5,
        "goal_priority": 4
    }
    """

    weights = {
        "time_horizon": 0.25,
        "income_stability": 0.15,
        "experience": 0.15,
        "loss_tolerance": 0.25,
        "goal_priority": 0.20
    }

    score = sum(answers[key] * weights[key] for key in answers)

    if score < 2:
        return "Conservative"
    elif score < 3:
        return "Balanced"
    elif score < 4:
        return "Moderate"
    elif score < 4.5:
        return "Growth"
    else:
        return "Aggressive"
