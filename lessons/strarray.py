"""Examples of vectgorized operations via magic methods."""

from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})."

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
            for item in self.items:
                result.items.append(item + rhs)
        else:
            assert len(self.items) == len(rhs.items)
            for i in range(len(self.items)):
                result.items.append(self.items[i] + rhs.items[i])
        return result

            # my attempt at doing something:
            # for i in self.items:
            #     i += rhs[i]
            #     result.items.append(i)

        # kj's proper explanation of how to add an "!" to each item in the list:
        # for i in self.items:
        #     i += rhs
        #     result.items.append(i)
        # return result
        
        # my first attempt for adding an "!" to each item in the list:
        # for i in self.items:
        #     self.items[i] += rhs
        #     result.items.append(self.items[i])
        # return result


a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + b)
print(a + " " + b)
print(b + ", " + a + "!")