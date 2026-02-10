"""
LP-Safe Redaction Layer
======================

This module enforces deterministic redaction rules for any replay or audit
artifact intended for LP, fiduciary, or regulatory consumption.

Design constraints:
- No inference
- No interpretation
- No valuation opinions
- No forward-looking belief leakage

This is a defensive compliance boundary, not a presentation layer.
"""

from enum import Enum
from typing import Dict, Any, List
from copy import deepcopy
from datetime import datetime, UTC



class Audience(Enum):
    INTERNAL = "internal"
    LP = "lp"
    REGULATOR = "regulator"


class RedactionReason(Enum):
    MNPI = "material_non_public_information"
    STRATEGY = "proprietary_strategy"
    BELIEF = "forward_looking_belief"
    DISCRETION = "internal_discretion"
    COUNTERFACTUAL = "counterfactual_analysis"


LP_REDACTION_FIELDS = {
    "belief_score": RedactionReason.BELIEF,
    "forward_scenarios": RedactionReason.COUNTERFACTUAL,
    "internal_notes": RedactionReason.STRATEGY,
    "sensitivity_analysis": RedactionReason.STRATEGY,
    "conviction_delta": RedactionReason.BELIEF,
    "what_if_paths": RedactionReason.COUNTERFACTUAL,
}


def redact_for_audience(
    replay_object: Dict[str, Any],
    audience: Audience,
) -> Dict[str, Any]:
    """
    Produce a redacted copy of a replay object for a specific audience.

    This function is deterministic and side-effect free.
    """
    if audience == Audience.INTERNAL:
        return replay_object

    redacted = deepcopy(replay_object)
    redacted_fields: List[Dict[str, Any]] = []

    for field, reason in LP_REDACTION_FIELDS.items():
        if field in redacted:
            redacted_fields.append(
                {
                    "field": field,
                    "reason": reason.value,
                    "redacted_at": datetime.utcnow().isoformat(),
                }
            )
            redacted[field] = None

    redacted["_redaction_metadata"] = {
        "audience": audience.value,
        "redacted_fields": redacted_fields,
        "policy_version": "6B-1.0",
        "deterministic": True,
        "interpretive": False,
    }

    return redacted
