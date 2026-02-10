from engine.replay.lp_redaction import redact_for_audience, Audience
from engine.replay.cross_cycle_replay import build_cross_cycle_replay
from engine.replay.regulator_exports import export_regulator_json
from engine.replay.responsibility_attestation import attach_responsibility_attestation
from engine.replay.evidence_integrity import attach_integrity_signal


def test_step6_end_to_end():
    raw_artifact = {
        "timestamp": "2025-11-01T10:15:00",
        "cycle_id": "cycle_2025_q4",
        "event_type": "capital_hold_decision",
        "surface_facts": {
            "company": "AlphaTech",
            "runway_months": 9
        },
        "actions_taken": {
            "decision": "hold"
        },
        "belief_score": 0.72,
        "conviction_delta": "+0.18",
        "forward_scenarios": ["acquisition", "down_round"],
        "internal_notes": "Founder credibility risk emerging",
        "what_if_paths": ["inject bridge capital"]
    }

    # 6B — redaction
    redacted = redact_for_audience(raw_artifact, Audience.LP)
    assert redacted["belief_score"] is None
    assert redacted["internal_notes"] is None
    assert "_redaction_metadata" in redacted

    # 6C — replay
    replay = build_cross_cycle_replay([raw_artifact])
    assert replay["interpretive"] is False
    assert replay["advisory"] is False
    assert len(replay["entries"]) == 1

    # 6E — responsibility
    attested = attach_responsibility_attestation(
        replay,
        responsible_entity="General Partner"
    )
    assert "_responsibility_attestation" in attested
    assert attested["_responsibility_attestation"]["non_advisory"] is True

    # 6F — integrity
    sealed = attach_integrity_signal(attested)
    assert "_integrity_signal" in sealed
    assert "content_hash" in sealed["_integrity_signal"]

    # 6D — regulator export
    export = export_regulator_json(sealed)
    assert export["non_advisory"] is True
    assert export["interpretive"] is False
