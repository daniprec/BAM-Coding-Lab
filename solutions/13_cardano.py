import time

import pandas as pd


def list_cardano(limit: int) -> int:
    # Initialize list of solutions
    ls_cardano = []

    # Simplified Cardano's formula
    # 8a^3 + 15a^2 + 6a - 27cb^2 = 1

    for a in range(2, limit):
        for b in range(1, limit - a):
            # Following the formula above, we can skip the "c" loop
            c = (8 * a**3 + 15 * a**2 + 6 * a - 1) / (27 * b**2)
            # Check if c is positive
            if c <= 0:
                continue
            # Check if c is an integer
            if not c.is_integer():
                continue
            # Check the sum
            if (a + b + c) <= limit:
                ls_cardano.append((a, b, int(c)))

    return sorted(set(ls_cardano))


def croot(x: float) -> float:
    """We need to define the cube root function for negative numbers."""
    if x < 0:
        return -((-x) ** (1 / 3))
    else:
        return x ** (1 / 3)


def assert_cardano(a: int, b: int, c: int) -> bool:
    sol = croot(a + b * c ** (1 / 2)) + croot(a - b * c ** (1 / 2))
    if round(sol, 8) == 1:
        return True
    else:
        raise ValueError(f"Failed for {a}, {b}, {c}. Expected 1, got {sol}")


def main():
    # Test
    start = time.time()
    ls_cardano = list_cardano(1000)
    print("Answer should be 149")
    print(len(ls_cardano))
    print("Execution time:", time.time() - start)

    # Result
    start = time.time()
    ls_cardano = list_cardano(5000)
    print(len(ls_cardano))
    print("Execution time:", time.time() - start)

    # Ensure they are correct
    for a, b, c in ls_cardano:
        assert_cardano(a, b, c)

    # Store the result in a dataframe
    df_cardano = pd.DataFrame(ls_cardano, columns=["a", "b", "c"])
    df_cardano.to_csv("solutions/13_cardano.csv", index=False)


if __name__ == "__main__":
    main()
