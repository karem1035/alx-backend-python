#!/usr/bin/env python3
import asyncio
import time
# Import wait_n function from 1-concurrent_coroutines.py
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time per task for executingwait_n
    (n, max_delay).

    Parameters:
    - n (int): Number of tasks to execute concurrently.
    - max_delay (int): Maximum delay parameter for each task execution.

    Returns:
    - float: Average time per task in seconds.
    """
    start_time = time.time()  # Record the start time
    # Run wait_n asynchronously with asyncio.run()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time  # Calculate total execution time
    return total_time / n  # Return average time per task
