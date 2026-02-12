from engine.ledger.action_registry import ActionRegistry


def test_step10b_registry_mapping():
    registry = ActionRegistry()

    registry.register(
        artifact_hash="artifact123",
        action_id="action456",
        ledger_entry_hash="ledger789",
    )

    entry = registry.get("artifact123")

    assert entry["action_id"] == "action456"
    assert entry["ledger_entry_hash"] == "ledger789"
