"""My version of wordle."""
__author__ = "730484416"


def contains_char(secret_word: str, searching_char: str) -> bool:
    """Searching a word for a character in a word."""
    assert len(searching_char) == 1
    i: int = 0
    while i < len(secret_word):
        if secret_word[i] == searching_char:  # if the character being searched for exists at any index of the secret word, return true
            return True
        i += 1
    return False

def emojified(guessed_word: str, SECRET: str) -> str:
    """Comparing guessed word to secret word and printing out corresponding emojis."""
    assert len(guessed_word) == len(SECRET)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    correct_characters: str = ""
    i: int = 0
    while i < len(guessed_word):
        if guessed_word[i] == SECRET[i]:  # if a character exists in both guessed_word and SECRET at the same index, add green box
            correct_characters += GREEN_BOX
        elif contains_char(SECRET, guessed_word[i]):  # when contains_char returns true (that character at index i exists anywhere in the secret word), add yellow box
            correct_characters += YELLOW_BOX
        else:  # add white box if character at index i of guessed_word does not exist in the secret word at all
            correct_characters += WHITE_BOX
        i += 1
    return correct_characters

def input_guess(expected_length: int) -> str:
    """Assuring that the guessed word is the same length as the secret word."""
    guessed_word = input(F"Enter a {expected_length} character word: ")
    while len(guessed_word) != expected_length:
        guessed_word = input(F"That wasn't {expected_length} chars! Try again: ")
    return guessed_word

def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"
    i: int = 1
    win_or_lose: bool = True
    while i <= 6 and win_or_lose:
        print(f"=== Turn {i}/6 ===")
        guessed_word: str = input_guess(len(SECRET))  # making the string returned from the input_guess function a str variable to be used as parameter for emojified function
        print(emojified(guessed_word, SECRET))
        if guessed_word == SECRET:
            print(f"You won in {i}/6 turns!")
            win_or_lose = False  # when user guesses the secret word correctly, game ends as this breaks the loop
        i += 1
    if guessed_word != SECRET:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()