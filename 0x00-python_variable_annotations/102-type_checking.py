#!/usr/bin/env python3
"""This module defines a type-annotated function zoom_array."""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Creates a new list with elements repeated based on a factor.

    Args:
        lst (Tuple): The input tuple.
        factor (int, optional): The repetition factor. Defaults to 2.

    Returns:
        List: The new list with repeated elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
