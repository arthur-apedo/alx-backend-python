#!/usr/bin/env python3
"""
    Measuring runtime for four parallel Comprehensions
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        return time to run the comprehension
    """
    begin_t = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_t = time.perf_counter() - begin_t
    return end_t
