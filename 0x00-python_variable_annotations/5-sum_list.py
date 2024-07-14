#!/usr/bin/env python3
"""
    complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        returns sum of list elements
    """
    s = 0
    for ele in input_list:
        s += ele
    return s
