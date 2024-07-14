#!/usr/bin/env python3
"""
    Complex types -> make multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Returns a function that multiplies a float by the given multiplier
    """
    def multiplier_function(value: float) -> float:
        """
            returns multiplier function
        """
        return value * multiplier
    return multiplier_function
