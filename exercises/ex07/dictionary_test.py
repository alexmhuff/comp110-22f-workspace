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


def test_favorite_color_friends() -> None:
    """Testing the most common favorite color out of my friends."""
    fave_colors: dict[str, str] = {"Alex": "red", "Gemma": "green", "Madison": "green", "Kenza": "green", "Madeleine": "blue"}
    assert favorite_color(fave_colors) == "green"


def test_favorite_color_random() -> None:
    """Testing the most common color in a dictionary."""
    fave_colors: dict[str, str] = {"a": "yellow", "b": "blue", "c": "green", "d": "orange", "e": "orange"}
    assert favorite_color(fave_colors) == "orange"


def test_favorite_color_empty() -> None:
    """Testing an empty dictionary."""
    fave_colors: dict[str, str] = {}
    assert favorite_color(fave_colors) == ""


def test_count_jobs() -> None:
    """Testing counting the times each job appears in a list."""
    times: list[str] = ["doctor", "doctor", "teacher", "professor", "teacher"]
    assert count(times) == {"doctor": 2, "teacher": 2, "professor": 1}


def test_count_names() -> None:
    """Testing counting the times each name appears in a list."""
    times: list[str] = ["Emma", "Ella", "Anna", "Ella", "Ally", "Ally", "Ella"]
    assert count(times) == {"Emma": 1, "Ella": 3, "Anna": 1, "Ally": 2}


def test_count_empty() -> None:
    """Testing counting an empty list."""
    times: list[str] = []
    assert count(times) == {}