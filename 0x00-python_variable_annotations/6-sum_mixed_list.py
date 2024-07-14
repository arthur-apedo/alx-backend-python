#!/usr/bin/env python3
"""
    Complex types -mixed list
"""
from typing import List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        returns a float
    """
    return float(sum(mxd_lst))
