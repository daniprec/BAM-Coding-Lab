import time

# Step 1: We create a function to check whether
# a list of points is a Pythagorean triplet


def is_pythagorean(ls: list[int]) -> bool:
    # Check the list has three numbers
    if len(ls) != 3:
        return False
    # Check the numbers are all positive integers
    for num in ls:
        if type(num) != int:
            return False
        if num <= 0:
            return False
    # Sort the list - The highest value should be "c"
    ls_sorted = sorted(ls)
    # Extract the values from the list
    a, b, c = ls_sorted
    # Check if it satisfies a pythagorean triple
    if (a**2 + b**2) == c**2:
        return True
    else:
        return False


print(is_pythagorean([1, 2]))  # False - not three numbers
print(is_pythagorean([4.0, 3.0, 5.0]))  # False - float
print(is_pythagorean([0, 1, 1]))  # False - non positive
print(is_pythagorean([1, 2, 3]))  # False - not satisfy the equation
print(is_pythagorean([4, 3, 5]))  # True
print(is_pythagorean([4, 5, 3]))  # True

# ----------------------------------------------

# Step 2: Create a loop to check all possible triplets
# We first test its speed with a lower limit

print("\nIMPLEMENTATION 1\n")

limit = 100

# Initialize the list that will contain all triples
ls_triplets = []
# Initialize the count of iterations
niter = 0

# Bad implementation
time_start = time.time()
for c in range(1, limit):
    for b in range(1, limit):
        for a in range(1, limit):
            # Iteration count goes up
            niter += 1
            if (a + b + c) > limit:
                continue
            triplet = sorted([a, b, c])
            if is_pythagorean(triplet) and (triplet not in ls_triplets):
                ls_triplets.append(triplet)
time_end = time.time()

print(f"There are {len(ls_triplets)} triplets with a sum less than {limit}")
print(f"We performed {niter} iterations")  # Should be 99^3 iterations
print(f"Time taken: {time_end - time_start}")

# ----------------------------------------------

# Step 3: Improve the loop, make sure we count 17 triplets

print("\nIMPLEMENTATION 2\n")

limit = 500

# Initialize the list that will contain all triples
ls_triplets = []
# Initialize the count of iterations
niter = 0

# Better implementation: Know that c > b > a
time_start = time.time()
for c in range(1, limit):
    for b in range(1, c):
        for a in range(1, b):
            # Iteration count goes up
            niter += 1
            if (a + b + c) > limit:
                continue
            triplet = sorted([a, b, c])
            if is_pythagorean(triplet):
                ls_triplets.append(triplet)
time_end = time.time()


print(f"There are {len(ls_triplets)} triplets with a sum less than {limit}")
print(f"We performed {niter} iterations")
print(f"Time taken: {time_end - time_start}")

# ----------------------------------------------

# Step 4: Improve the loop even more

print("\nIMPLEMENTATION 3\n")

limit = 5000

# Initialize the list that will contain all triples
ls_triplets = []
# Initialize the count of iterations
niter = 0

# Better implementation: Know that c > b > a
time_start = time.time()
for c in range(1, limit):
    for b in range(1, min(limit - c, c)):
        # Iteration count goes up
        niter += 1
        a = (c**2 - b**2) ** 0.5
        if int(a) != a:
            continue
        if a > b:
            continue
        if (a + b + c) > limit:
            continue
        ls_triplets.append(sorted([a, b, c]))
time_end = time.time()

print(f"There are {len(ls_triplets)} triplets with a sum less than {limit}")
print(f"We performed {niter} iterations")
print(f"Time taken: {time_end - time_start}")
