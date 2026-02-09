import numpy as np

from typing import Tuple

from pe_core.domain.matrices import CapitalStateMatrix
from pe_core.domain.events import EventOperator


def propagate_event(
    matrix: CapitalStateMatrix,
    operator: EventOperator,
) -> CapitalStateMatrix:
    """
    Applies an event operator to all capital states in a portfolio.

    This function does not interpret results.
    It only propagates structural change.
    """
    new_states = matrix.matrix @ operator.transform.T
    return CapitalStateMatrix(new_states)
