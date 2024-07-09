#!/usr/bin/env python3
"""
    Basic syntax:
        Program takes in an integer(max_delay=10)
        Waits for a random delay between 0 and max delay

"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    res = random.uniform(0, max_delay)
    await asyncio.sleep(res)
    return res
