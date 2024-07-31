#!/usr/bin/env python3
'''8. Complex types - functions'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def mult_func(fl: float) -> float:
        return multiplier * fl

    return mult_func
