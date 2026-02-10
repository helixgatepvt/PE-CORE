"""
Evidence Integrity & Tamper Signal
=================================

Attaches a deterministic integrity signal to artifacts intended for
LP, regulator, or audit distribution.

This module does not sign, encrypt, or notarize.
It simply makes post-hoc modification detectable.
"""

from typing import Dict, Any
from datetime import datetime
import hashlib
import json


INTEGRITY_POLICY_VERSION = "6F-1.0"
HASH_ALGORITHM = "sha256"


def _canonical_serialize(payload: Dict[str, Any]) -> str:
    """
    Canonical JSON serialization to ensure deterministic hashing.
    """
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    )


def attach_integrity_signal(
    artifact: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Compute and attach an integrity hash to an artifact.

    The hash is computed over the artifact *excluding* any existing
    integrity block to avoid recursive mutation.
    """

    artifact_copy = dict(artifact)
    artifact_copy.pop("_integrity_signal", None)

    serialized = _canonical_serialize(artifact_copy)
    digest = hashlib.sha256(serialized.encode("utf-8")).hexdigest()

    artifact["_integrity_signal"] = {
        "policy_version": INTEGRITY_POLICY_VERSION,
        "hash_algorithm": HASH_ALGORITHM,
        "content_hash": digest,
        "generated_at": datetime.utcnow().isoformat(),
        "canonicalization": "json_sorted_keys_no_whitespace",
        "tamper_evident": True,
    }

    return artifact
