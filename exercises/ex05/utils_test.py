"""Unit testing list functions."""
__author__ = "730484416"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Testing only_evens when the list is empty."""
    list_1: list[int] = []
    assert only_evens(list_1) == []


def test_only_evens_all_evens() -> None:
    """Testing only_evens when the list is all evens."""
    list_1: list[int] = [2, 4, 6]
    assert only_evens(list_1) == [2, 4, 6]


def test_only_evens_all_odds() -> None:
    """Testing only_evens when the list is all odds."""
    list_1: list[int] = [5, 7, 9]
    assert only_evens(list_1) == []


def test_only_evens_mixed() -> None:
    """Testing only_evens when the list has odds and evens."""
    list_1: list[int] = [1, 3, 4, 5, 6, 8]
    assert only_evens(list_1) == [4, 6, 8]


def test_concat_empty() -> None:
    """Testing concat when both lists are empty."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_list_1_empty() -> None:
    """Testing concat when list_1 is empty."""
    list_1: list[int] = []
    list_2: list[int] = [2, 3, 4]
    assert concat(list_1, list_2) == [2, 3, 4]


def test_concat_list_2_empty() -> None:
    """Testing concat when list_2 is empty."""
    list_1: list[int] = [4, 5, 6]
    list_2: list[int] = []
    assert concat(list_1, list_2) == [4, 5, 6]


def test_concat_full_lists_one() -> None:
    """Testing concat when both lists are full."""
    list_1: list[int] = [3, 2]
    list_2: list[int] = [5, 1, 14]
    assert concat(list_1, list_2) == [3, 2, 5, 1, 14]


def test_concat_full_lists_two() -> None:
    """Testing concat when both lists are full."""
    list_1: list[int] = [4, 6, 1]
    list_2: list[int] = [2, 3]
    assert concat(list_1, list_2) == [4, 6, 1, 2, 3]


def test_sub_empty() -> None:
    """Testing sub when the list is empty."""
    list_1: list[int] = []
    start: int = 1
    end: int = 3
    assert sub(list_1, start, end) == []


def test_sub_two_six() -> None:
    """Testing sub when starting at index 2 and ending at index 6."""
    list_1: list[int] = [4, 7, 65, 23, 56, 7, 3]
    start: int = 2
    end: int = 6
    assert sub(list_1, start, end) == [65, 23, 56, 7]


def test_sub_four_seven() -> None:
    """Testing sub when starting at index 4 and ending at index 7."""
    list_1: list[int] = [3, 4, 5, 6, 7, 8, 9, 0, 11]
    start: int = 4
    end: int = 7
    assert sub(list_1, start, end) == [7, 8, 9]


def test_sub_negative_start() -> None:
    """Testing sub when the start index is negative."""
    list_1: list[int] = [1, 2, 3, 4, 5]
    start: int = -4
    end: int = 3
    assert sub(list_1, start, end) == [1, 2, 3]


def test_sub_negative_end() -> None:
    """Testing sub when the end index is negative."""
    list_1: list[int] = [2, 3, 4, 6, 7, 8]
    start: int = 1
    end: int = -2
    assert sub(list_1, start, end) == []


def test_sub_larger_end() -> None:
    """Testing sub when the end index is too large."""
    list_1: list[int] = [2, 3, 4, 6, 7, 8]
    start: int = 1
    end: int = 8
    assert sub(list_1, start, end) == []