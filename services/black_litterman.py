from pypfopt import risk_models, expected_returns
from pypfopt.efficient_frontier import EfficientFrontier
import numpy as np

def optimize_black_litterman(price_data, market_caps):
    """
    Simplified Black-Litterman:
    - Avoids PyPortfolioOpt BlackLittermanModel (buggy for Python 3.10+)
    - Computes equilibrium returns using CAPM × market cap weights
    """

    # Covariance matrix
    S = risk_models.CovarianceShrinkage(price_data).ledoit_wolf()

    # CAPM returns for tickers
    capm_returns = expected_returns.capm_return(price_data)

    # Market cap weights
    tickers = list(price_data.columns)
    mcaps = np.array([market_caps[t] for t in tickers], dtype=float)
    mcaps = mcaps / mcaps.sum()

    # Equilibrium returns (BL without views)
    pi = capm_returns * mcaps

    # Optimize using MPT with equilibrium returns
    ef = EfficientFrontier(pi, S)
    ef.max_sharpe()

    return {
        "weights": ef.clean_weights(),
        "performance": ef.portfolio_performance(verbose=False)
    }
