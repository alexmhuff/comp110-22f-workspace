"""'list' Utility Functions."""
__author__ = "7304416"


def all(list: list[int], match: int) -> bool:
    """Find if one integer matches all integers in a list."""
    if len(list) == 0:
        return False
    i: int = 0
    i2: int = 0
    while i < len(list):
        if list[i] == match:
            i2 += 1
        i += 1
    if i2 == len(list):
        return True
    else:
        return False


def max(list: list[int]) -> int:
    """Find the highest number in a list."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max: int = list[0]
    while i < len(list):
        if list[i] > max:
            max = list[i]
        i += 1
    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Find if two lists match entirely."""
    if list_1 == list_2:
        return True
    else:
        return False