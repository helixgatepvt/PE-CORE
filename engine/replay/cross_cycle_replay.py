"""
Cross-Cycle Belief Replay (LP-Safe)
==================================

Produces a time-ordered, redacted replay of belief states across
multiple capital cycles for LP or regulator review.

Constraints:
- No belief scoring
- No delta computation
- No interpretation
- No hindsight optimization

This module exists solely to demonstrate temporal consistency
and fiduciary process integrity.
"""

from typing import List, Dict, Any
from datetime import datetime

from engine.replay.lp_redaction import redact_for_audience, Audience


def build_cross_cycle_replay(
    replay_objects: List[Dict[str, Any]],
    audience: Audience = Audience.LP,
) -> Dict[str, Any]:
    """
    Construct a cross-cycle replay timeline suitable for LP consumption.

    Input:
        replay_objects: unordered list of replay artifacts

    Output:
        deterministic, time-ordered replay timeline
    """

    normalized = []

    for obj in replay_objects:
        timestamp = obj.get("timestamp")
        if not timestamp:
            raise ValueError("Replay object missing timestamp")

        try:
            parsed_time = datetime.fromisoformat(timestamp)
        except Exception:
            raise ValueError(f"Invalid timestamp format: {timestamp}")

        redacted = redact_for_audience(obj, audience)

        normalized.append(
            {
                "timestamp": parsed_time.isoformat(),
                "cycle_id": obj.get("cycle_id"),
                "event_type": obj.get("event_type"),
                "surface_facts": redacted.get("surface_facts"),
                "actions_taken": redacted.get("actions_taken"),
                "redaction_metadata": redacted.get("_redaction_metadata"),
            }
        )

    normalized.sort(key=lambda x: x["timestamp"])

    return {
        "audience": audience.value,
        "replay_type": "cross_cycle_belief_replay",
        "generated_at": datetime.utcnow().isoformat(),
        "entries": normalized,
        "interpretive": False,
        "advisory": False,
    }
