import pytest

from engine.governance.capital_gate import (
    validate_capital_action,
    CapitalGateViolation,
)


def test_step7_blocks_missing_integrity():
    bad_artifact = {}

    with pytest.raises(CapitalGateViolation):
        validate_capital_action(bad_artifact)


def test_step7_blocks_interpretive_artifact():
    bad_artifact = {
        "_integrity_signal": {"content_hash": "abc"},
        "_responsibility_attestation": {
            "non_advisory": True,
            "non_reliance": True,
        },
        "interpretive": True,
    }

    with pytest.raises(CapitalGateViolation):
        validate_capital_action(bad_artifact)


def test_step7_allows_valid_artifact():
    valid_artifact = {
        "_integrity_signal": {"content_hash": "abc"},
        "_responsibility_attestation": {
            "non_advisory": True,
            "non_reliance": True,
        },
        "interpretive": False,
    }

    # Should not raise
    validate_capital_action(valid_artifact)
