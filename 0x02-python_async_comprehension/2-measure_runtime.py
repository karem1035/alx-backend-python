#!/usr/bin/env python3
"""
Module to measure the runtime of asyncio_comprehension() function.

The runtime measurement is done by creating 4 tasks and waiting for all of them
to complete. The runtime is then calculated by subtracting the start time from
the current time.
"""
from typing import List
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> List[float]:
    """
    Measures the runtime of asyncio_comprehension() function for 4 tasks.

    Returns:
        List[float]: A list of runtime values per task.
    """
    # Start time of the measurement
    start_time = time.time()

    # Create a list of tasks by calling asyncio_comprehension() function
    # for each task in range(4)
    tasks: List = [async_comprehension() for _ in range(4)]

    # Wait for all tasks to complete using asyncio.gather()
    await asyncio.gather(*tasks)

    # Calculate the runtime of each task by subtracting the start time
    # from the current time
    runtime: List[float] = [time.time() - start_time for _ in range(4)]

    return runtime
