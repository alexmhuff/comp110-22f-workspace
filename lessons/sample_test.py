"""words"""
from audioop import avg


quiz1: int=100
quiz2: int=98
quiz3: int=84
final: avg=(quiz1+quiz2+quiz3)/3
print("Ready to learn your final?")
print("You received "print(quiz1)" on your first quiz")
print("You received "print(quiz2)" on your second quiz")
print("You received "print(quiz3)" on your third quiz")
print("Your final grade is "print(final)"")