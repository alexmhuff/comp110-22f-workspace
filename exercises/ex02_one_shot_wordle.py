"""One shot wordle."""
__author__ = "730484416"

SECRET: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
correct_characters: str = ""
guessed_word: str = input(F"What is your {len(SECRET)}-letter guess? ")
while len(guessed_word) != len(SECRET):  # loop until user guesses a 6-letter word
    guessed_word = input(F"That was not {len(SECRET)} letters! Try again: ")

if len(guessed_word) == len(SECRET): 
    if guessed_word != SECRET:
        while i < len(guessed_word):
            evaluating: bool = False
            if guessed_word[i] != SECRET[i]:  # if the initial location of a character in guessed_word doesn't match the correseponding location in SECRET
                i2: int = 0
                while i2 < len(SECRET):
                    if guessed_word[i] == SECRET[i2]:  # checking if the character in guessed_word exists in any location of SECRET
                        evaluating = True
                    i2 += 1  # breaks the checking-all-locations of SECRET loop
                if evaluating:  # because evaluating is already defined as true, this says if true it'll keep going
                    correct_characters = correct_characters + YELLOW_BOX
                else:
                    correct_characters = correct_characters + WHITE_BOX
            else:
                correct_characters = correct_characters + GREEN_BOX
            i += 1  # breaks the checking-each-character of guessed_word loop
        print(correct_characters)
        print("Not quite. Play again soon!")     
    else:
        while i < len(guessed_word):
            if SECRET[i] == guessed_word[i]:
                correct_characters = correct_characters + GREEN_BOX
                i += 1
        print(correct_characters)
        print("Woo! You got it!")