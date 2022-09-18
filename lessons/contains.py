"""An example of a list utility algorithm."""

# name: contains
# function w 2 parameters:
#  needle - what we're searching for
#  haystack - what we're searching through
# return type: bool

def contains(needle: str, haystack: list[str]) -> bool:
    # start from first index
    i: int = 0
    # loop through each index of the list
    while i < len(haystack):
        # test if the item at this index is equal to the needle
        if haystack[i] == needle:
            # yes! return true
            return True
        i += 1
    # return false
    return False