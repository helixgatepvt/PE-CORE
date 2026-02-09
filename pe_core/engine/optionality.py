import numpy as np


def optionality_decay(
    initial_optionality: float,
    decay_rate: float,
    delay: float,
) -> float:
    """
    Computes time-asymmetric optionality decay.

    initial_optionality:
        Starting degree of freedom (normalized).

    decay_rate:
        Composite friction parameter (governance, liquidity, constraints).

    delay:
        Time elapsed before decision or action.

    This function performs NO optimization and NO prediction.
    """
    return initial_optionality * np.exp(-decay_rate * delay)
