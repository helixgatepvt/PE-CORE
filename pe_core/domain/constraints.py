from typing import Callable, List

from .vectors import CapitalStateVector


# A constraint returns a float.
# <= 0  → constraint satisfied
# >  0  → constraint violated
Constraint = Callable[[CapitalStateVector], float]


class ConstraintSet:
    """
    Collection of hard constraints defining the admissible
    region of capital state space.
    """

    def __init__(self, constraints: List[Constraint]):
        self.constraints = constraints

    def violated(self, state: CapitalStateVector) -> bool:
        """
        Returns True if any constraint is violated.
        """
        return any(constraint(state) > 0 for constraint in self.constraints)

    def violation_values(self, state: CapitalStateVector) -> List[float]:
        """
        Returns the raw violation magnitudes for all constraints.
        """
        return [constraint(state) for constraint in self.constraints]
