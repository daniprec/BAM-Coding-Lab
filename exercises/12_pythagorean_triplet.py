# Step 1: We create a function to check whether
# a list of points is a Pythagorean triplet


def is_pythagorean(ls: list) -> bool:
    # Check the list has three numbers
    pass
    # Check the numbers are all positive integers
    pass
    # Sort the list - The highest value should be "c"
    pass
    # Extract the values from the list
    pass
    # Check if it satisfies a pythagorean triple
    pass


print(is_pythagorean([1, 2]))  # False - not three numbers
print(is_pythagorean([4.0, 3.0, 5.0]))  # False - float
print(is_pythagorean([0, 1, 1]))  # False - non positive
print(is_pythagorean([1, 2, 3]))  # False - not satisfy the equation
print(is_pythagorean([4, 3, 5]))  # True
print(is_pythagorean([4, 5, 3]))  # True

# ----------------------------------------------

# Step 2: Create a loop to check all possible triplets
# We first test its speed with a lower limit

limit = 100

# Initialize the list that will contain all triples
ls_triplets = []
# Initialize the count of iterations
niter = 0

# Bad implementation
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

print(f"There are {len(ls_triplets)}")
print(f"We performed {niter} iterations")  # Should be 99^3 iterations

# ----------------------------------------------

# Step 3: Optimize the loop!

# ----------------------------------------------

# BONUS: Implement a function that generates a Cardano triplet
# Fill in the code in challenges/12_cardano_triplet.py
