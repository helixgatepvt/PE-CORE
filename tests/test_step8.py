import pytest
import hashlib
import json

from engine.execution.capital_execution import execute_capital_action
from engine.governance.capital_gate import CapitalGateViolation


def _build_valid_artifact():
    base = {
        "_responsibility_attestation": {
            "non_advisory": True,
            "non_reliance": True,
        },
        "interpretive": False,
    }

    serialized = json.dumps(
        base,
        sort_keys=True,
        separators=(",", ":"),
    )

    content_hash = hashlib.sha256(serialized.encode()).hexdigest()

    return {
        **base,
        "_integrity_signal": {"content_hash": content_hash},
    }


def test_step8_executes_valid_action():
    artifact = _build_valid_artifact()

    record = execute_capital_action(
        artifact,
        action_type="capital_call",
        amount=1000000.0,
        currency="USD",
    )

    assert record["governance_validated"] is True
    assert record["artifact_hash"] == artifact["_integrity_signal"]["content_hash"]
    assert "action_id" in record


def test_step8_blocks_invalid_artifact():
    with pytest.raises(CapitalGateViolation):
        execute_capital_action({}, "capital_call", 1000, "USD")
