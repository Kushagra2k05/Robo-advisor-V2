def backtest_portfolio(price_data, weights):
    returns = price_data.pct_change().dropna()
    portfolio_returns = (returns * list(weights.values())).sum(axis=1)
    cumulative = (1 + portfolio_returns).cumprod()
    return cumulative
