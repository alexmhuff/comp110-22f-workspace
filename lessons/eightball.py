"""Programming an eightball in class."""

from random import randint #function that python language provides to us -- allows us to randint

question: str = input("Ask a yes/no question...") #doesn't even need to be a variable
response: int = randint(0,2) #bounds for the random integer -- you can see required syntax/set up when you start typing the parentheses

if response == 0:
    print("Yes, definitely") #could use this to pull a name out of a hat
else:
    if response == 1: 
        print("Ask again later")
    else: 
        if response == 2:
            print("You betcha")
        else:
            print("My sources say no")

#shift/tab unindents
#nesting if/else in a more concise way:

if response == 0:
    print("Most definitely")
elif response == 1:
    print("Ask again later")
elif response == 2:
    print("You betcha")
else:
    print("My sources say no")