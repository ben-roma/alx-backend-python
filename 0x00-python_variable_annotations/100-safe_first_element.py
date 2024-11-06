#!/usr/bin/env python3
"""This module defines a type-annotated function safe_first_element."""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Retrieves the first element of a sequence if it exists.

    Args:
        lst (Sequence[Any]): A sequence of any type.

    Returns:
        Union[Any, None]: The first element of the sequence or None
                          if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
