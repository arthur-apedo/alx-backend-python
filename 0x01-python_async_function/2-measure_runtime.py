#!/usr/bin/env python3
"""
    Measure the runtime
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def m_time(n: int, max_delay: int) -> float:

    """
        returns the total execution time for wait_n and returns
        total_time / n
    """
    begin_time = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - begin_time
    res = total_time / n
    return res


def measure_time(n: int, max_delay: int) -> float:
    """
         runs m_time
    """
    return asyncio.run(m_time(n, max_delay))
