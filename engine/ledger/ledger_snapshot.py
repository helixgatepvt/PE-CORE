"""
Step 10A — Ledger Snapshot (Anchored + Versioned)
"""

import hashlib
import json
from typing import List, Dict, Any, Optional


SNAPSHOT_VERSION = "10A-2.0"


def _canonical_serialize(payload: Dict[str, Any]) -> str:
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    )


def generate_ledger_snapshot(
    ledger_entries: List[Dict[str, Any]],
    previous_snapshot_hash: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Deterministic snapshot of ledger state.

    Supports anchoring to previous snapshot hash.
    """

    snapshot_payload = {
        "snapshot_version": SNAPSHOT_VERSION,
        "entry_count": len(ledger_entries),
        "entries": ledger_entries,
        "previous_snapshot_hash": previous_snapshot_hash,
    }

    serialized = _canonical_serialize(snapshot_payload)
    snapshot_hash = hashlib.sha256(serialized.encode()).hexdigest()

    return {
        "snapshot_version": SNAPSHOT_VERSION,
        "entry_count": len(ledger_entries),
        "snapshot_hash": snapshot_hash,
        "previous_snapshot_hash": previous_snapshot_hash,
    }
