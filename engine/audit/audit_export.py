"""
Step 10C — Audit Export Surface
===============================
Produces institution-safe audit exports.
"""

from typing import Dict, Any

from engine.ledger.capital_ledger import CapitalLedger
from engine.ledger.ledger_snapshot import generate_ledger_snapshot


def generate_audit_report(ledger: CapitalLedger) -> Dict[str, Any]:
    snapshot = generate_ledger_snapshot(ledger)

    return {
        "report_type": "capital_audit",
        "ledger_snapshot": snapshot,
        "attestation": {
            "non_advisory": True,
            "non_interpretive": True,
        },
    }
