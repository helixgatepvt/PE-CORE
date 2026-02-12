"""
Step 9 — Immutable Capital Ledger
==================================
Append-only, hash-chained ledger for capital actions.
"""

import hashlib
import json
from typing import Dict, Any, List


class LedgerIntegrityError(Exception):
    pass


class CapitalLedger:
    def __init__(self):
        self._entries: List[Dict[str, Any]] = []

    def _compute_entry_hash(self, entry: Dict[str, Any]) -> str:
        serialized = json.dumps(
            entry,
            sort_keys=True,
            separators=(",", ":"),
        )
        return hashlib.sha256(serialized.encode()).hexdigest()

    def append(self, execution_record: Dict[str, Any]) -> Dict[str, Any]:
        previous_hash = (
            self._entries[-1]["entry_hash"]
            if self._entries
            else "GENESIS"
        )

        ledger_entry = {
            "previous_hash": previous_hash,
            "execution_record": execution_record,
        }

        entry_hash = self._compute_entry_hash(ledger_entry)

        ledger_entry["entry_hash"] = entry_hash
        self._entries.append(ledger_entry)

        return ledger_entry

    def verify_integrity(self) -> None:
        for i, entry in enumerate(self._entries):
            expected_hash = self._compute_entry_hash(
                {
                    "previous_hash": entry["previous_hash"],
                    "execution_record": entry["execution_record"],
                }
            )

            if entry["entry_hash"] != expected_hash:
                raise LedgerIntegrityError(
                    f"Ledger entry {i} hash mismatch."
                )

            if i > 0:
                if entry["previous_hash"] != self._entries[i - 1]["entry_hash"]:
                    raise LedgerIntegrityError(
                        f"Ledger chain broken at entry {i}."
                    )

    def entries(self) -> List[Dict[str, Any]]:
        return list(self._entries)
        
