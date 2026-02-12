import hashlib
import json
from typing import List, Dict, Any


def generate_ledger_snapshot(ledger_entries: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generate a deterministic snapshot hash of the ledger state.
    """

    serialized = json.dumps(
        ledger_entries,
        sort_keys=True,
        separators=(",", ":"),
    )

    snapshot_hash = hashlib.sha256(serialized.encode()).hexdigest()

    return {
        "entry_count": len(ledger_entries),
        "snapshot_hash": snapshot_hash,
    }
