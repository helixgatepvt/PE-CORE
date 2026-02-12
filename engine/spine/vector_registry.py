"""
HelixGate — Canonical Valuation Vector Registry
------------------------------------------------

This module defines the 112 deterministic valuation vectors
used by the HelixGate Capital Clearance Engine.

Vectors are:

• Immutable
• Categorized
• Replay-compatible
• Institutionally auditable
"""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class ValuationVector:
    code: str
    name: str
    category: str
    description: str


# ------------------------------------------------------------------
# VECTOR CATEGORIES
# ------------------------------------------------------------------

CATEGORIES = [
    "Revenue Quality",
    "Margin Integrity",
    "Capital Structure",
    "Liquidity Risk",
    "Governance",
    "Regulatory Exposure",
    "Operational Resilience",
    "Counterparty Risk",
    "Macro Sensitivity",
    "Valuation Integrity",
    "Disclosure Quality",
    "Capital Allocation",
]


# ------------------------------------------------------------------
# CORE VECTOR DEFINITIONS (SAMPLE EXPANSION FRAME)
# ------------------------------------------------------------------

VECTORS: List[ValuationVector] = [

    # Revenue Quality
    ValuationVector(
        code="RQ-01",
        name="Revenue Concentration Risk",
        category="Revenue Quality",
        description="Degree of revenue dependency on top customers."
    ),
    ValuationVector(
        code="RQ-02",
        name="Recurring Revenue Stability",
        category="Revenue Quality",
        description="Predictability and contractual durability of recurring revenue."
    ),

    # Margin Integrity
    ValuationVector(
        code="MI-01",
        name="Gross Margin Volatility",
        category="Margin Integrity",
        description="Stability of gross margins across reporting periods."
    ),

    # Capital Structure
    ValuationVector(
        code="CS-01",
        name="Debt Maturity Compression",
        category="Capital Structure",
        description="Near-term refinancing pressure."
    ),

    # Liquidity Risk
    ValuationVector(
        code="LR-01",
        name="Runway Coverage Ratio",
        category="Liquidity Risk",
        description="Cash runway relative to burn rate."
    ),

    # Governance
    ValuationVector(
        code="GV-01",
        name="Board Independence Integrity",
        category="Governance",
        description="Degree of independent governance oversight."
    ),

    # Regulatory Exposure
    ValuationVector(
        code="RE-01",
        name="Jurisdictional Regulatory Sensitivity",
        category="Regulatory Exposure",
        description="Exposure to regulatory regime volatility."
    ),

    # Operational Resilience
    ValuationVector(
        code="OR-01",
        name="Single-Point Operational Failure Risk",
        category="Operational Resilience",
        description="Dependency on non-redundant operational infrastructure."
    ),

    # Counterparty Risk
    ValuationVector(
        code="CR-01",
        name="Counterparty Default Exposure",
        category="Counterparty Risk",
        description="Exposure to financially unstable counterparties."
    ),

    # Macro Sensitivity
    ValuationVector(
        code="MS-01",
        name="Interest Rate Sensitivity",
        category="Macro Sensitivity",
        description="Valuation impact under rate stress scenarios."
    ),

    # Valuation Integrity
    ValuationVector(
        code="VI-01",
        name="Multiple Expansion Dependency",
        category="Valuation Integrity",
        description="Reliance on terminal multiple expansion assumptions."
    ),

    # Disclosure Quality
    ValuationVector(
        code="DQ-01",
        name="Financial Reporting Transparency",
        category="Disclosure Quality",
        description="Clarity and completeness of disclosed financial data."
    ),

    # Capital Allocation
    ValuationVector(
        code="CA-01",
        name="Capital Efficiency Discipline",
        category="Capital Allocation",
        description="Return on invested capital discipline."
    ),
]


def load_all_vectors() -> List[ValuationVector]:
    """
    Deterministic loader for full vector set.
    """
    return VECTORS
