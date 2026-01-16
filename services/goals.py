def calculate_sip(goal_amount, years, expected_return=0.12, inflation=0.05):
    adj_rate = ((1 + expected_return) / (1 + inflation)) - 1
    months = years * 12
    r = adj_rate / 12

    sip = goal_amount * r / ((1 + r)**months - 1)
    return round(sip, 2)
