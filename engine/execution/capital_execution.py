"""
Step 8 — Capital Action Binding & Execution Record
===================================================

This module binds a validated Step 6 artifact
to a capital action and creates an execution record.
"""

import hashlib
import json
from datetime import datetime, UTC
from typing import Dict, Any

from engine.governance.capital_gate import validate_capital_action


class CapitalExecutionError(Exception):
    pass


def execute_capital_action(
    step6_artifact: Dict[str, Any],
    action_type: str,
    amount: float,
    currency: str,
) -> Dict[str, Any]:
    """
    Execute a capital action after Step 7 validation.
    Returns execution receipt.
    """

    # Enforce Step 7 validation
    validate_capital_action(step6_artifact)

    integrity_block = step6_artifact["_integrity_signal"]
    artifact_hash = integrity_block["content_hash"]

    execution_timestamp = datetime.now(UTC).isoformat()

    # Deterministic action ID
    action_payload = {
        "artifact_hash": artifact_hash,
        "action_type": action_type,
        "amount": amount,
        "currency": currency,
        "timestamp": execution_timestamp,
    }

    serialized = json.dumps(
        action_payload,
        sort_keys=True,
        separators=(",", ":"),
    )

    action_id = hashlib.sha256(serialized.encode()).hexdigest()

    execution_record = {
        "action_id": action_id,
        "artifact_hash": artifact_hash,
        "action_type": action_type,
        "amount": amount,
        "currency": currency,
        "executed_at": execution_timestamp,
        "governance_validated": True,
    }

    return execution_record

