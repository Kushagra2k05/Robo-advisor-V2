from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage
from pypfopt.efficient_frontier import EfficientFrontier

def optimize_mpt(price_data):
    mu = mean_historical_return(price_data)
    S = CovarianceShrinkage(price_data).ledoit_wolf()

    ef = EfficientFrontier(mu, S)
    ef.max_sharpe()

    return {
        "weights": ef.clean_weights(),
        "performance": ef.portfolio_performance(verbose=False)
    }
