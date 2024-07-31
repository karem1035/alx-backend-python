#!/usr/bin/env python3
'''Complex types - string and int/float to tuple'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''return a tuple out of 2 arguments'''
    return (k, float(v ** 2))
