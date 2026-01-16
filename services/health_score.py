def calculate_health_score(weights, volatility, diversification_score):
    score = (
        (1 - volatility) * 0.4 +
        diversification_score * 0.4 +
        sum(weights.values()) * 0.2
    )
    return round(score * 100, 2)
