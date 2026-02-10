def generate_governance_report(compliance):
    return {
        "title": "Governance Compliance Record",
        "status": compliance["compliance_status"],
        "violations": compliance.get("violations", []),
        "evaluated_at": compliance.get("evaluated_at")
    }
