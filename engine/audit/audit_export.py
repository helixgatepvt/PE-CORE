from typing import Dict, Any

from engine.ledger.capital_ledger import CapitalLedger
from engine.ledger.ledger_snapshot import generate_ledger_snapshot


def generate_audit_report(ledger: CapitalLedger) -> Dict[str, Any]:
    """
    Produce an institution-safe audit export.
    """

    # 1️⃣ Verify ledger integrity first
    ledger.verify_integrity()

    # 2️⃣ Get immutable entries
    ledger_entries = ledger.entries()

    # 3️⃣ Generate deterministic snapshot
    snapshot = generate_ledger_snapshot(ledger_entries)

    # 4️⃣ Attach verification signal
    snapshot["verified"] = True

    return {
        "report_type": "capital_audit",
        "ledger_snapshot": snapshot,
        "attestation": {
            "non_advisory": True,
            "non_interpretive": True,
        },
    }
