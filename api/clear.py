from engine.ccm.clearance_engine import generate_clearance
from engine.ccm.fee_record import calculate_ccm_fee

def clear_capital(deal_id, snapshot, deployed_capital):
    clearance = generate_clearance(snapshot, deployed_capital)
    fee = calculate_ccm_fee(deployed_capital)

    # persist clearance + fee in DB (pseudo)
    save_clearance(clearance)
    save_fee(fee)

    return {
        "clearance": clearance,
        "fee": fee
    }

