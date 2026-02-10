ENGINE_VERSION = "hg-ccm-v1.0.0"

def generate_clearance(snapshot, deployed_capital):
    issues = snapshot.get("unresolved_constraints", [])
    risks = snapshot.get("risk_vector", [])

    if issues:
        status = "CONDITIONAL"
    else:
        status = "CLEARED"

    return {
        "clearance_status": status,
        "conditions": issues,
        "accepted_risks": risks,
        "deployed_capital_amount": deployed_capital,
        "engine_version_hash": ENGINE_VERSION
    }

