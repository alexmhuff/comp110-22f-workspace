"""Unit testing dictionary functions."""
__author__ = "730484416"

from dictionary import invert, favorite_color, count


def test_invert_sisters() -> None:
    """Testing a pair of names inverting."""
    given_dict: dict[str, str] = {"Alex": "Brooke", "Ava": "Anna"}
    assert invert(given_dict) == {"Brooke": "Alex", "Anna": "Ava"}


def test_invert_classes() -> None:
    """Testing a class and its start time inverting."""
    given_dict: dict[str, str] = {"COMP110": "12:30", "WGST224": "10:10", "RELI106": "12:20", "RELI209": "2:00"}
    assert invert(given_dict) == {"12:30": "COMP110", "10:10": "WGST224", "12:20": "RELI106", "2:00": "RELI209"}


def test_invert_empty() -> None:
    """Testing if a given dictionary is empty that it will result empty."""
    given_dict: dict[str, str] = {}
    assert invert(given_dict) == {}


# favorite colors example: {a: green, b: blue, c: green, d: purple, e: blue}
#