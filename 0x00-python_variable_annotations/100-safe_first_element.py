#!/usr/bin/env python3
"""
    Duck-typed annotaions for safe_first_element function
"""
from typing import Sequence, Any Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        Returnd the fist element of the list if it exists, otherwise returns None
    """
    if lst:
        return lst[0]
    else:
        return None
