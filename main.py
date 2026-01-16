from services.risk_profile import calculate_risk_profile
from services.price_fetcher import fetch_price_data
from services.mpt_optimizer import optimize_mpt
from services.black_litterman import optimize_black_litterman
from services.goals import calculate_sip
from services.monte_carlo import monte_carlo_sim
from services.rebalance import rebalance_portfolio
from config.assets import MARKET_CAPS

def main():
    answers = {
        "time_horizon": 4,
        "income_stability": 3,
        "experience": 3,
        "loss_tolerance": 4,
        "goal_priority": 5
    }

    profile = calculate_risk_profile(answers)
    print("Risk Profile:", profile)

    risk_assets = {
        "Conservative": ["BND", "AGG", "VOO"],
        "Balanced": ["VOO", "AGG", "QQQ"],
        "Moderate": ["VOO", "QQQ", "IWM"],
        "Growth": ["QQQ", "IWM", "EFA"],
        "Aggressive": ["QQQ", "ARKK", "ETH-USD"]
    }

    tickers = risk_assets[profile]
    price_data = fetch_price_data(tickers)

    # MPT Optimization
    mpt_result = optimize_mpt(price_data)
    print("\nMPT Weights:", mpt_result["weights"])

    # Black-Litterman Optimization
    bl_result = optimize_black_litterman(price_data, MARKET_CAPS)
    print("\nBlack-Litterman Weights:", bl_result["weights"])

    # Goal planning
    sip = calculate_sip(5000000, 10)
    print("\nRequired SIP for goal:", sip)

    # Monte Carlo
    mc = monte_carlo_sim(100000, 0.08, 0.15, 5)
    print("\nMonte Carlo sample result:", mc[:5])

    # Rebalance
    rebalance = rebalance_portfolio(
        target_weights=mpt_result["weights"],
        current_weights={"VOO": 0.3, "QQQ": 0.2, "IWM": 0.1},
        portfolio_value=300000
    )
    print("\nRebalancing actions:", rebalance)

if __name__ == "__main__":
    main()
