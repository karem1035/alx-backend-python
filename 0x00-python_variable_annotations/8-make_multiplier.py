#!/usr/bin/env python3
'''8. Complex types - functions'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Multiplies a given float value by the multiplier.
    """
    def mult_func(fl: float) -> float:
        """
        Multiplies the given float value `fl` by the multiplier.
        """
        return multiplier * fl

    return mult_func
