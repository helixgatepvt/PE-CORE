"""
Regulator Export Formats
=======================

Serializes replay artifacts into regulator-consumable formats.

Design principles:
- Evidence over explanation
- Determinism over narrative
- Process visibility without strategy leakage

This module produces exports suitable for SEC, FCA, and audit review.
"""

from typing import Dict, Any, List
from datetime import datetime
import json


EXPORT_POLICY_VERSION = "6D-1.0"


def export_regulator_json(
    cross_cycle_replay: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Produce a canonical JSON export for regulators.

    This output is designed to be archived, hashed, and reviewed.
    """

    return {
        "export_type": "regulator_json",
        "policy_version": EXPORT_POLICY_VERSION,
        "generated_at": datetime.utcnow().isoformat(),
        "non_advisory": True,
        "interpretive": False,
        "source_replay": cross_cycle_replay.get("replay_type"),
        "audience": cross_cycle_replay.get("audience"),
        "entries": cross_cycle_replay.get("entries", []),
    }


def export_regulator_csv_rows(
    cross_cycle_replay: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """
    Flatten replay entries into CSV-compatible rows.

    Intended for ingestion into regulator tooling, not human analysis.
    """

    rows = []

    for entry in cross_cycle_replay.get("entries", []):
        rows.append(
            {
                "timestamp": entry.get("timestamp"),
                "cycle_id": entry.get("cycle_id"),
                "event_type": entry.get("event_type"),
                "surface_facts": json.dumps(entry.get("surface_facts")),
                "actions_taken": json.dumps(entry.get("actions_taken")),
                "redaction_policy": entry.get("redaction_metadata", {}).get(
                    "policy_version"
                ),
            }
        )

    return rows
