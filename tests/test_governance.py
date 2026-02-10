from importlib import import_module

evaluate_compliance = import_module(
    "engine.governance.enforcement_engine"
).evaluate_compliance


def test_compliant_decision():
    snapshot = {
        "assumptions_vector": ["market growth"],
        "accepted_risks": ["regulatory"]
    }

    mandate = {
        "required_snapshot": True,
        "required_assumptions": True,
        "required_risk_acceptance": True
    }

    result = evaluate_compliance(snapshot, mandate)

    assert result["compliance_status"] == "COMPLIANT"
    assert result["violations"] == []


def test_non_compliant_missing_assumptions():
    snapshot = {
        "accepted_risks": ["customer concentration"]
    }

    mandate = {
        "required_snapshot": True,
        "required_assumptions": True,
        "required_risk_acceptance": True
    }

    result = evaluate_compliance(snapshot, mandate)

    assert result["compliance_status"] == "NON_COMPLIANT"
    assert "Missing assumptions" in result["violations"]
