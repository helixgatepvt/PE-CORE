import numpy as np

from .vectors import CapitalStateVector, VECTOR_DIMENSION


class EventOperator:
    """
    Canonical transformation operator for capital state vectors.

    Each event is represented as a (112 x 112) transformation matrix.
    Event operators are non-commutative by design.
    """

    def __init__(self, transform: np.ndarray):
        if transform.shape != (VECTOR_DIMENSION, VECTOR_DIMENSION):
            raise ValueError(
                f"EventOperator must be a {VECTOR_DIMENSION}x{VECTOR_DIMENSION} matrix"
            )

        self.transform = transform

    def apply(self, state: CapitalStateVector) -> CapitalStateVector:
        """
        Applies the event transformation to a capital state.
        """
        new_values = self.transform @ state.values
        return CapitalStateVector(new_values)
