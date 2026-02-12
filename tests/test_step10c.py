from engine.ledger.capital_ledger import CapitalLedger
from engine.audit.audit_export import generate_audit_report


def test_step10c_audit_export():
    ledger = CapitalLedger()
    ledger.append({"action_id": "a1"})

    report = generate_audit_report(ledger)

    assert report["report_type"] == "capital_audit"
    assert report["ledger_snapshot"]["verified"] is True
