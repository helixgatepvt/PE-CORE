"""
Responsibility & Non-Reliance Attestation Layer
==============================================

This module enforces explicit fiduciary responsibility boundaries
for all HelixGate artifacts exposed to LPs, regulators, or auditors.

It is not legal advice.
It is a system-level boundary declaration.
"""

from typing import Dict, Any
from datetime import datetime, UTC


ATTESTATION_POLICY_VERSION = "6E-1.0"


def attach_responsibility_attestation(
    artifact: Dict[str, Any],
    responsible_entity: str,
) -> Dict[str, Any]:
    """
    Attach a non-reliance and responsibility attestation to an artifact.

    This function must be applied before any external distribution.
    """

    attestation = {
        "policy_version": ATTESTATION_POLICY_VERSION,
        "generated_at": datetime.utcnow().isoformat(),
        "non_advisory": True,
        "non_reliance": True,
        "no_recommendation": True,
        "no_decision_making": True,
        "no_fiduciary_assumption": True,
        "responsibility_retained_by": responsible_entity,
        "system_role": "process_intelligence_and_recordkeeping_only",
    }

    artifact["_responsibility_attestation"] = attestation
    return artifact
