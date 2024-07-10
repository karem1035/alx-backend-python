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

    Example Usage:
    ```python
    import asyncio
    from your_module import task_wait_n

    async def main():
        delays = await task_wait_n(5, 10)
        print(f"Sorted delays: {delays}")

    asyncio.run(main())
    ```
    """
    # Gather results from multiple task_wait_random tasks
    resolved = await asyncio.gather(
        *(task_wait_random(max_delay) for i in range(n))
    )
    # Return the sorted list of results
    return sorted(resolved)
