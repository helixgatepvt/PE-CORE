"""
HelixGate — Portfolio Clearance Engine
---------------------------------------
Aggregates composite vector scores and produces
a deterministic capital clearance decision.
"""

from typing import List
from dataclasses import dataclass

from .vector_scoring import CompositeVectorScore
from .vector_registry import load_all_vectors


@dataclass(frozen=True)
class ClearanceDecision:
    status: str
    critical_count: int
    elevated_count: int
    liquidity_critical: bool


class PortfolioClearanceEngine:

    def __init__(self):
        self.registry = {v.code: v for v in load_all_vectors()}

    def evaluate(self, scores: List[CompositeVectorScore]) -> ClearanceDecision:

        critical = 0
        elevated = 0
        liquidity_critical = False

        for score in scores:

            if score.risk_band == "CRITICAL":
                critical += 1

                vector = self.registry.get(score.vector_code)
                if vector and vector.category == "Liquidity Risk":
                    liquidity_critical = True

            elif score.risk_band == "ELEVATED":
                elevated += 1

        # ---- Deterministic Gating Rules ----

        if liquidity_critical:
            status = "BLOCK"

        elif critical >= 3:
            status = "BLOCK"

        elif elevated >= 5:
            status = "CONDITIONAL"

        else:
            status = "CLEAR"

        return ClearanceDecision(
            status=status,
            critical_count=critical,
            elevated_count=elevated,
            liquidity_critical=liquidity_critical,
        )
