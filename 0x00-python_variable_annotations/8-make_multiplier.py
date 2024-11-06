#!/usr/bin/env python3
"""This module defines a type-annotated function make_multiplier that takes a
float multiplier as argument and returns a function that multiplies a float
by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float as input
                                 and returns the product of the input
                                 and the multiplier.
    """

    def multiplier_function(x: float) -> float:
        """
        Multiplies a float by the multiplier.

        Args:
            x (float): The float to multiply.

        Returns:
            float: The product of x and the multiplier.
        """
        return x * multiplier

    return multiplier_function
