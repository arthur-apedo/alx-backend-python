#!/usr/bin/env python3
"""
    Executing multiple coroutines
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        return a sorted list of all delays
    """
    lst = []
    for i in range(0, n):
        delay = await wait_random(max_delay)
        lst.append(delay)

    sorted_lst = []
    while lst:
        min_delay = min(lst)
        lst.remove(min_delay)
        sorted_lst.append(min_delay)
    return sorted_lst
