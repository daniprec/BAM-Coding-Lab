# REVIEW OF COMPUTER PROGRAMMING 1

# Lets refresh Python functions, loops and flow control.
# Look at the following pieces of code and fix them!


def power(a: int, b: int) -> int:
    result = a**b
    # The return statement was missing
    return result


print(power(2, 3))  # 8

# ----------------------------------------------


def factorial(n: int) -> int:
    # We must initialize the result to 1
    # because we are multiplying!
    result = 1
    # The range should go up to n+1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(4))  # 24

# ----------------------------------------------


def power_or_factorial(a: int, b: int = None) -> int:
    # b is not None, it is 0 by default
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
        # The condition should be num % 2 == 0
        # Remember that // is integer division
        if num % 2 == 0:
            n_even += 1
        else:
            # Should be summing up the odd numbers
            n_odd += 1
    # We want to return both counts, not the sum!
    return n_even, n_odd


print(count_even_and_odd([1, 2, 3, 4, 5]))  # (2, 3)
