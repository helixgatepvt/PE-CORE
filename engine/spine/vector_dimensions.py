"""
HelixGate — Vector Dimensional Framework
------------------------------------------

Defines the canonical 7 evaluation dimensions
applied to all 112 valuation vectors.
"""

from dataclasses import dataclass
from typing import Dict, List


DIMENSIONS: List[str] = [
    "severity",
    "probability",
    "persistence",
    "reversibility",
    "contagion",
    "transparency",
    "controlability",
]


@dataclass(frozen=True)
class VectorAssessment:
    """
    Represents a 7-dimensional evaluation of a single vector.
    Scores are normalized on a 0–5 scale.
    """

    vector_code: str
    scores: Dict[str, float]

    def validate(self):
        for dim in DIMENSIONS:
            if dim not in self.scores:
                raise ValueError(f"Missing dimension: {dim}")

            value = self.scores[dim]

            if not (0.0 <= value <= 5.0):
                raise ValueError(
                    f"Dimension '{dim}' must be between 0 and 5."
                )

