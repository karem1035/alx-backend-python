#!/usr/bin/env python3

"""executing multiple coroutines at the same time with async"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """This return a list of delays"""
    delays = []
    tasks = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    gathered = await asyncio.gather(*tasks)
    delays.extend(gathered)
    return delays
