def evaluate_compliance(snapshot, mandate):
    violations = []

    if mandate["required_snapshot"] and not snapshot:
        violations.append("Missing decision snapshot")

    if mandate["required_assumptions"] and not snapshot.get("assumptions_vector"):
        violations.append("Missing assumptions")

    if mandate["required_risk_acceptance"] and not snapshot.get("accepted_risks"):
        violations.append("Missing risk acceptance")

    status = "COMPLIANT" if not violations else "NON_COMPLIANT"

    return {
        "compliance_status": status,
        "violations": violations
    }
