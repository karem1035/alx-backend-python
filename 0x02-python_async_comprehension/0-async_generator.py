#!/usr/bin/env python3
"""Module uses generator to return a random float between 0 and 10."""
import asyncio
import random


async def async_generator():
    """
    An asynchronous generator that yields random float values.

    yields 10 random float values between 0 and 10, with a 1-second
    delay between each yield.

    Yields:
        float: A random float value between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
