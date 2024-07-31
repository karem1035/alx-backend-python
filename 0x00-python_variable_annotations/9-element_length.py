#!/usr/bin/env python3
'''Let's duck type an iterable object'''
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the given iterable of sequences.

    Parameters:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains a sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
