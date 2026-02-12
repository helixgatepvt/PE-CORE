"""
Step 10B — Artifact to Action Registry
======================================
Maintains deterministic mapping between artifacts and capital actions.
"""

from typing import Dict, Any


class ActionRegistry:
    def __init__(self):
        self._registry: Dict[str, Dict[str, str]] = {}

    def register(
        self,
        artifact_hash: str,
        action_id: str,
        ledger_entry_hash: str,
    ) -> None:
        self._registry[artifact_hash] = {
            "action_id": action_id,
            "ledger_entry_hash": ledger_entry_hash,
        }

    def get(self, artifact_hash: str) -> Dict[str, str]:
        return self._registry[artifact_hash]

    def entries(self) -> Dict[str, Dict[str, str]]:
        return dict(self._registry)

