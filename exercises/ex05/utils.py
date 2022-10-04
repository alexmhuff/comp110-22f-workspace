"""Creating list functions to unit test."""
__author__ = "730484416"


def only_evens(list_1: list[int]) -> list[int]:
    """Selecting only even numbers from a list of integers."""
    return_list: list[int] = []
    i: int = 0
    while i < len(list_1):
        if list_1[i] % 2 == 0:
            return_list.append(list_1[i])
        i += 1
    return return_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Concatenation one list to another."""
    new_list: list[int] = []
    i: int = 0
    while i < len(list_1):
        new_list.append(list_1[i])
        i += 1
    i = 0
    while i < len(list_2):
        new_list.append(list_2[i])
        i += 1
    return new_list


def sub(list_1: list[int], start: int, end: int) -> list[int]:
    """Taking a subset of numbers from a list with a given range."""
    new_list: list[int] = []
    i: int = 0
    if start < 0:
        start = 0
    if end < 0:
        return []
    if end > len(list_1):
        end = len(list_1)
    if start > len(list_1):
        return []
    while i < len(list_1):
        if i >= start and i < end:
            new_list.append(list_1[i])
        i += 1
    return new_list