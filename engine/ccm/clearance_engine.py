ENGINE_VERSION = "hg-ccm-v1.0.0"

def generate_clearance(snapshot, deployed_capital):
    unresolved_conditions = snapshot.get("unresolved_conditions", [])
    accepted_risks = snapshot.get("risk_vector", [])

    if unresolved_conditions:
        status = "CONDITIONAL"
    else:
        status = "CLEARED"

    return {
        "clearance_status": status,
        "conditions": unresolved_conditions,
        "accepted_risks": accepted_risks,
        "deployed_capital_amount": deployed_capital,
        "engine_version_hash": ENGINE_VERSION
    }
