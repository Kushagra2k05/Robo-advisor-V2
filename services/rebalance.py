def rebalance_portfolio(target_weights, current_weights, portfolio_value):
    actions = {}

    for asset, target in target_weights.items():
        curr = current_weights.get(asset, 0)
        diff = target - curr
        actions[asset] = round(diff * portfolio_value, 2)

    return actions
