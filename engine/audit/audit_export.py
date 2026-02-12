"""
Step 10C — Exportable Audit Surface
===================================

Generates an institutional-grade audit report that binds:

- Ledger entries
- Ledger snapshot hash
- Entry count
- Deterministic export structure

This module must remain read-only relative to the ledger.
"""

from typing import List, Dict, Any
from datetime import datetime, UTC


def generate_audit_report(ledger_entries: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generate a deterministic audit report for the current ledger state.
    """

    # Local import to avoid circular dependency
    from engine.ledger.ledger_snapshot import generate_ledger_snapshot

    snapshot = generate_ledger_snapshot(ledger_entries)

    return {
        "generated_at": datetime.now(UTC).isoformat(),
        "ledger_entry_count": snapshot["entry_count"],
        "ledger_snapshot_hash": snapshot["snapshot_hash"],
        "ledger_entries": ledger_entries,
        "deterministic": True,
        "interpretive": False,
    }
