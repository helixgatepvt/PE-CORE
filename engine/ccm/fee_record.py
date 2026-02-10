def calculate_ccm_fee(deployed_capital, rate=0.02):
    return {
        "deployed_capital_amount": deployed_capital,
        "fee_rate": rate,
        "calculated_fee": deployed_capital * rate,
        "fee_status": "RECORDED"
    }

