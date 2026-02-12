"""
Step 10C — Institutional Audit Export
=====================================
Produces anchored, cross-validated audit surface.
"""

from typing import Dict, Any, Optional

from engine.ledger.capital_ledger import CapitalLedger
from engine.ledger.ledger_snapshot import generate_ledger_snapshot
from engine.ledger.action_registry import ActionRegistry


def generate_audit_report(
    ledger: CapitalLedger,
    registry: ActionRegistry,
    previous_snapshot_hash: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Institutional-grade audit export.
    """

    # 1️⃣ Verify ledger integrity
    ledger.verify_integrity()

    ledger_entries = ledger.entries()

    # 2️⃣ Cross-validate registry ↔ ledger
    registry.validate_ledger_consistency(ledger_entries)

    # 3️⃣ Generate anchored snapshot
    snapshot = generate_ledger_snapshot(
        ledger_entries,
        previous_snapshot_hash=previous_snapshot_hash,
    )

    snapshot["verified"] = True

    return {
        "report_type": "capital_audit",
        "ledger_snapshot": snapshot,
        "registry_size": len(registry.entries()),
        "cross_validated": True,
        "attestation": {
            "non_advisory": True,
            "non_interpretive": True,
        },
    }
