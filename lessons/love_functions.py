"""Some tender, loving functions."""


def love(subject: str) -> str:  # looks like variable because it's similar, saying "love" is going to return a string
    """Given a subject as a parameter, returns a loving string."""
    return f"I love you {subject}!"  # nothing would happen if we ran this -- there's no call

love("Kris")  # still no output -- there's no print or input function

print(love("Alex"))  # print result of love and then your name ? -- Alex = subject: str, function is simply the return of the string "I love you subject"
#  so f"I love you {subject}!" replaces (love("Alex"))

# from "lessons.name" import "function"

def spread_love(to: str, n: int) -> str:  # n = number of times we'll return a message
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n" # TODO: the real work
        # love function, to as argument
        i += 1
    return love_note