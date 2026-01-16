import numpy as np

def monte_carlo_sim(initial_value, mean, std, years, trials=1000):
    results = []

    for _ in range(trials):
        value = initial_value
        for _ in range(years):
            value *= np.random.normal(1 + mean, std)
        results.append(value)

    return results
