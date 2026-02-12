"""
Step 5E — Internal Sensitivity & Distribution Classification
============================================================

This module classifies replay artifacts at creation time.

It declares sensitivity and distribution constraints.
It does not redact, export, interpret, or enforce.
"""

from enum import Enum
from typing import Dict, Any, List
from datetime import datetime, UTC



class SensitivityLevel(Enum):
    INTERNAL_ONLY = "internal_only"
    GP_CONFIDENTIAL = "gp_confidential"
    LP_ELIGIBLE = "lp_eligible"


class ContentFlag(Enum):
    MNPI = "material_non_public_information"
    BELIEF = "belief_mechanics"
    STRATEGY = "proprietary_strategy"
    COUNTERFACTUAL = "counterfactual_analysis"
    OPERATIONAL = "operational_fact"


CLASSIFICATION_POLICY_VERSION = "5E-1.0"


def classify_artifact(
    artifact: Dict[str, Any],
    sensitivity: SensitivityLevel,
    content_flags: List[ContentFlag],
) -> Dict[str, Any]:
    """
    Attach sensitivity and distribution classification to a replay artifact.

    This MUST be applied before any Step 6 processing.
    """

    artifact["_sensitivity"] = {
        "level": sensitivity.value,
        "content_flags": [flag.value for flag in content_flags],
        "external_distribution_allowed": (
            sensitivity == SensitivityLevel.LP_ELIGIBLE
        ),
        "policy_version": CLASSIFICATION_POLICY_VERSION,
        "classified_at": datetime.now(UTC).isoformat(),
        "step": "5E",
    }

    return artifact
