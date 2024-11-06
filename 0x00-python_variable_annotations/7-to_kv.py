#!/usr/bin/env python3
"""This module defines a type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple. The first element of
the tuple is the string k. The second element is the square of the int/float
v and should be annotated as a float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with a string and the square of an int/float.

    Args:
        k (str): The string value.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple with the string and the square of the
                           int/float as a float.
    """
    return (k, float(v ** 2))
