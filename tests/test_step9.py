import pytest

from engine.ledger.capital_ledger import (
    CapitalLedger,
    LedgerIntegrityError,
)


def test_step9_append_and_verify():
    ledger = CapitalLedger()

    record1 = {"action_id": "a1"}
    record2 = {"action_id": "a2"}

    ledger.append(record1)
    ledger.append(record2)

    # Should not raise
    ledger.verify_integrity()


def test_step9_detects_tampering():
    ledger = CapitalLedger()

    record = {"action_id": "a1"}
    entry = ledger.append(record)

    # Tamper with execution record
    entry["execution_record"]["action_id"] = "tampered"

    with pytest.raises(LedgerIntegrityError):
        ledger.verify_integrity()
        
