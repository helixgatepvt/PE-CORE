from typing import Dict

from .constraints import ConstraintSet
from .events import EventOperator


class JurisdictionProfile:
    """
    Defines how capital behaves under a specific jurisdictional regime.

    This class does NOT encode law.
    It binds:
    - constraint sets
    - event operator variants
    """

    def __init__(
        self,
        name: str,
        constraints: ConstraintSet,
        event_operators: Dict[str, EventOperator],
    ):
        self.name = name
        self.constraints = constraints
        self.event_operators = event_operators
