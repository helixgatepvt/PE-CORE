"""
Step 10B — Artifact to Action Registry
======================================
Maintains deterministic mapping between artifacts and capital actions.
Adds ledger cross-validation enforcement.
"""

from typing import Dict, Any, List


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

    def validate_ledger_consistency(
        self,
        ledger_entries: List[Dict[str, Any]],
    ) -> None:
        """
        Ensure every execution_record in ledger has a registered action_id.
        """
        registered_action_ids = {
            entry["action_id"]
            for entry in self._registry.values()
        }

        for entry in ledger_entries:
            execution = entry.get("execution_record", {})
            action_id = execution.get("action_id")

            if action_id not in registered_action_ids:
                raise ValueError(
                    f"Unregistered action_id in ledger: {action_id}"
                )
