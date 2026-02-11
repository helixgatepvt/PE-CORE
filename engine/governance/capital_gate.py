"""
Step 7 — Capital Allocation Boundary Enforcement
=================================================

This module enforces that no capital action may proceed
without a valid, sealed Step 6 artifact.
"""

from typing import Dict, Any


class CapitalGateViolation(Exception):
    """Raised when capital boundary enforcement fails."""
    pass


def validate_capital_action(step6_artifact: Dict[str, Any]) -> None:
    """
    Validate that a capital decision is allowed to proceed.

    Raises CapitalGateViolation if any required condition fails.
    """

    # Must contain integrity signal
    if "_integrity_signal" not in step6_artifact:
        raise CapitalGateViolation("Missing integrity signal.")

    # Must contain responsibility attestation
    if "_responsibility_attestation" not in step6_artifact:
        raise CapitalGateViolation("Missing responsibility attestation.")

    attestation = step6_artifact["_responsibility_attestation"]

    if not attestation.get("non_advisory", False):
        raise CapitalGateViolation("Artifact is advisory.")

    if not attestation.get("non_reliance", False):
        raise CapitalGateViolation("Artifact lacks non-reliance clause.")

    # Must be non-interpretive
    if step6_artifact.get("interpretive", True):
        raise CapitalGateViolation("Artifact is interpretive.")

    # Must not expose forbidden fields
    forbidden_fields = [
        "belief_score",
        "conviction_delta",
        "forward_scenarios",
        "internal_notes",
        "what_if_paths",
    ]

    for field in forbidden_fields:
        if field in step6_artifact and step6_artifact[field] is not None:
            raise CapitalGateViolation(f"Forbidden field present: {field}")
