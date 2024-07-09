#!/usr/bin/env python3
"""executing multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple instances of the `wait_random` coroutine concurrently.

    Parameters:
    - n (int): Number of times to execute the `wait_random` coroutine.
    - max_delay (int): Maximum delay parameter for the `wait_random` coroutine.

    Returns:
    - list[float]: A list of delays (float values) sorted in ascending order.
    """
    resolved = await asyncio.gather(
        *(wait_random(max_delay) for i in range(n)))
    return sorted(resolved)
