from engine.ccm.clearance_engine import generate_clearance

def test_clearance_without_issues():
    snapshot = {
        "unresolved_constraints": [],
        "risk_vector": ["market", "regulatory"]
    }

    result = generate_clearance(snapshot, deployed_capital=10_000_000)

    assert result["clearance_status"] == "CLEARED"
    assert result["deployed_capital_amount"] == 10_000_000


def test_clearance_with_conditions():
    snapshot = {
        "unresolved_constraints": ["Missing customer concentration disclosure"],
        "risk_vector": ["customer"]
    }

    result = generate_clearance(snapshot, deployed_capital=5_000_000)

    assert result["clearance_status"] == "CONDITIONAL"
    assert len(result["conditions"]) == 1
    
