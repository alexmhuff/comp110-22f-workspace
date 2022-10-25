"""Idk yet."""
__author__: "730484416"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Inverting the key and value of a list."""
    result: dict[str, str] = {}
    for key in given_dict:
        if given_dict[key] in result:
            raise KeyError("You can't have the same key twice!")
        result[given_dict[key]] = key
    return result


def favorite_color(fave_colors: dict[str, str]) -> str:
    """Taking a dictionary and returning the most common value."""
    result: dict[str, int] = {}
    for key in fave_colors:
        if fave_colors[key] in result:
            result[fave_colors[key]] += 1
        else:
            result[fave_colors[key]] = 1
    largest_count: int = 0
    most_common: str = ""
    for key in result:
        if result[key] > largest_count:
            largest_count = result[key]
            most_common = key
    return most_common


def count(times: list[str]) -> dict[str, int]:
    """Counting how many times each item occurs in a list."""
    result: dict[str, int] = {}
    for i in times:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result