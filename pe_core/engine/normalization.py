from typing import Dict

import numpy as np

from pe_core.domain.vectors import CapitalStateVector, VECTOR_DIMENSION


def normalize_disclosure(disclosure: Dict[int, float]) -> CapitalStateVector:
    """
    Normalizes raw disclosure data into a canonical 112D capital state vector.

    disclosure:
        A mapping from vector index → value.
        Missing indices are set to zero by default.

    This function performs NO inference and NO validation.
    """
    values = np.zeros(VECTOR_DIMENSION)

    for index, value in disclosure.items():
        if 0 <= index < VECTOR_DIMENSION:
            values[index] = value

    return CapitalStateVector(values)
