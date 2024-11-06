#!/usr/bin/env python3
"""This module defines a type-annotated function floor which takes a float n
as argument and returns the floor of the float.
"""


import math


def floor(n: float) -> int:
    """
    Calculates the floor of a float.

    Args:
        n (float): The float number.

    Returns:
        int: The floor of the float.
    """
    return math.floor(n)
