import matplotlib.pyplot as plt
import numpy as np

# Step 1: Implement the Bezier function


def bezier_cubic(
    p0: tuple, p1: tuple, p2: tuple, p3: tuple, n_points: int = 100
) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate a cubic Bézier curve with four control points
    """
    # Initialize the parameter t
    pass
    # Compute the curve
    pass
    # Extract the x and y coordinates
    pass


# Lets try it out with some control points

# Generate the curve and plot it

# Plot the control points on it


# ----------------------------------------------

# Step 2: Implement a function to compute the area under a curve
# and the length of that curve


def area_under_curve(x: np.array, y: np.array) -> float:
    """Approximage the area under a curve using the trapezoidal rule"""
    pass


def length_of_curve(x: np.array, y: np.array) -> float:
    """Approximage the length of a curve using the distance formula"""
    pass


# Lets try it out with (y = 1 - x)

# The area w.r.t. the axes is 0.5

# Its length is sqrt(2) ~= 1.414

# ----------------------------------------------

# Step 3: Test functions with some sample control points

# Define a v, generate a Bézier curve with it

# Compute the area and length of the curve

# Plot the curve and the control points

# Draw an actual quarter circle


# ----------------------------------------------
# BONUS: Implement a function to generate a Bezier curve
# for any degree (any number of control points)
# Fill in the code in challenges/13_bezier_hd.py
