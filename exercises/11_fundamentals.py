# REVIEW OF COMPUTER PROGRAMMING 1

# Lets refresh Python functions, loops and flow control.
# Look at the following pieces of code and fix them!


def power(a: int, b: int) -> int:
    result = a**b


print(power(2, 3))  # 8

# ----------------------------------------------


def factorial(n: int) -> int:
    result = 0
    for i in range(1, n):
        result *= i
    return result


print(factorial(4))  # 24

# ----------------------------------------------


def power_or_factorial(a: int, b: int = 0) -> int:
    if b is None:
        return factorial(a)
    else:
        return power(a, b)


print(power_or_factorial(2))  # 2
print(power_or_factorial(2, 3))  # 8

# ----------------------------------------------


def count_even_and_odd(ls: list) -> tuple:
    n_even = 0
    n_odd = 0
    for num in ls:
        if num // 2 == 0:
            n_even += 1
        else:
            n_odd -= 1
    return n_even + n_odd


print(count_even_and_odd([1, 2, 3, 4, 5]))  # (2, 3)
