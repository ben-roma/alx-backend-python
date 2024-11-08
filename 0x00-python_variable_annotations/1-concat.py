#!/usr/bin/env python3
"""This module defines a type-annotated function concat that takes a string
str1 and a string str2 as arguments and returns a concatenated string.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return str1 + str2
