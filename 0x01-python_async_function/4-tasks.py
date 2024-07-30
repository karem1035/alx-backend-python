#!/usr/bin/env python3
"""
This module contains an async function to execute multiple tasks concurrently.
"""

import asyncio
from typing import List

# Import the task_wait_random function from the 3-tasks module
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple tasks concurrently and return their results sorted.

    Args:
    - n (int): The number of tasks to create.
    - max_delay (int): The maximum delay in seconds for each task.

    Returns:
    - List[float]: A list of delays in ascending order.
    """
    resolved = await asyncio.gather(
        *(task_wait_random(max_delay) for i in range(n))
    )
    return sorted(resolved)
