#!/usr/bin/env python3
"""Asynchronously processes 10 random floats yielding a list."""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously processes 10 random float values between 0 and 10
    using an async generator, yielding the values as a list of floats.

    :return: A list of 10 random float values between 0 and 10.
    :rtype: List[float]
    """
    return [_ async for _ in async_generator()]
