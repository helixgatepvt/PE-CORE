from engine.replay.lp_redaction import redact_for_audience, Audience
from engine.replay.cross_cycle_replay import build_cross_cycle_replay
from engine.replay.regulator_exports import export_regulator_json
from engine.replay.responsibility_attestation import attach_responsibility_attestation
from engine.replay.evidence_integrity import attach_integrity_signal

# ---- Step 5 UNSAFE artifact (intentionally) ----
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

print("\n--- RAW ARTIFACT (UNSAFE) ---")
print(raw_artifact)

# ---- 6B: Redaction ----
redacted = redact_for_audience(raw_artifact, Audience.LP)

print("\n--- AFTER 6B (REDACTED) ---")
print(redacted)

# ---- 6C: Cross-cycle replay ----
replay = build_cross_cycle_replay([raw_artifact])

print("\n--- AFTER 6C (REPLAY) ---")
print(replay)

# ---- 6E: Responsibility Attestation ----
attested = attach_responsibility_attestation(
    replay,
    responsible_entity="General Partner"
)

print("\n--- AFTER 6E (RESPONSIBILITY ATTACHED) ---")
print(attested)

# ---- 6F: Integrity Signal ----
sealed = attach_integrity_signal(attested)

print("\n--- AFTER 6F (INTEGRITY SEALED) ---")
print(sealed)

# ---- 6D: Regulator Export ----
export = export_regulator_json(sealed)

print("\n--- FINAL REGULATOR EXPORT ---")
print(export)
