"""EX01 - Chardle - a cute step toward wordle."""
__author__ = "730484416"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) > 5:
    print("Error: Word must contain 5 characters.")
    exit()
if len(five_character_word) < 5:
    print("Error: Word must contain 5 characters.")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
instances_counter: int = 0
print(F"Searching for {single_character} in " + five_character_word)
if single_character == five_character_word[0]:
    instances_counter = instances_counter + 1
    print(single_character + " found at index 0")
if single_character == five_character_word[1]:
    instances_counter = instances_counter + 1
    print(single_character + " found at index 1")
if single_character == five_character_word[2]:
    instances_counter = instances_counter + 1
    print(single_character + " found at index 2")
if single_character == five_character_word[3]:
    instances_counter = instances_counter + 1
    print(single_character + " found at index 3")
if single_character == five_character_word[4]:
    instances_counter = instances_counter + 1
    print(single_character + " found at index 4")
if instances_counter == 0:
    print("No instances of " + single_character + " found in " + five_character_word)
if instances_counter == 1:
    print("1 instance of " + single_character + " found in " + five_character_word)
if instances_counter == 2:
    print("2 instances of " + single_character + " found in " + five_character_word)
if instances_counter == 3:
    print("3 instances of " + single_character + " found in " + five_character_word)
if instances_counter == 4:
    print("4 instances of " + single_character + " found in " + five_character_word)
if instances_counter == 5:
    print("5 instances of " + single_character + " found in " + five_character_word)