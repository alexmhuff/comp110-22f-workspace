# x: int = 1

# def f(y: int) -> int:
#     return x + y

# print(f(x + 1))

x: int = 0

def f() -> None:
    x: int = 1

f()
print(x)