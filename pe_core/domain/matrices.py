import numpy as np
from typing import Final

from .vectors import VECTOR_DIMENSION


class CapitalStateMatrix:
    """
    Canonical portfolio-level container for capital state vectors.

    Shape: (n, 112)
    Each row corresponds to one CapitalStateVector.
    """

    def __init__(self, states: np.ndarray):
        if states.ndim != 2:
            raise ValueError("CapitalStateMatrix must be a 2D array")

        if states.shape[1] != VECTOR_DIMENSION:
            raise ValueError(
                f"Each capital state must be {VECTOR_DIMENSION}-dimensional"
            )

        self.matrix: Final[np.ndarray] = states
