#!/usr/bin/env python3
"""
    Running tasks
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        return a sorted list of all delays
    """
    lst = []
    for i in range(0, n):
        delay = await task_wait_random(max_delay)
        lst.append(delay)

    sorted_lst = []
    while lst:
        min_delay = min(lst)
        lst.remove(min_delay)
        sorted_lst.append(min_delay)
    return sorted_lst
