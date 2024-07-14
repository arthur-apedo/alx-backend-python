#!/usr/bin/env python3
"""
    Element length function with type annotations
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Returns a list of tuples, where each tuple contains an element
        of the input iterable and its length
    """
    return [(i, len(i)) for i in lst]
