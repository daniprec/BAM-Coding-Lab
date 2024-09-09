import matplotlib.pyplot as plt
import numpy as np

# Step 1: Implement the Bezier function


def bezier_cubic(p0: tuple, p1: tuple, p2: tuple, p3: tuple, n_points: int = 100):
    """
    Generate a cubic Bézier curve with four control points
    """
    t = np.linspace(0, 1, n_points).reshape(-1, 1)
    curve = (
        (np.power(1 - t, 3) * p0)
        + (3 * np.power(1 - t, 2) * t * p1)
        + (3 * (1 - t) * np.power(t, 2) * p2)
        + (np.power(t, 3) * p3)
    )
    x = curve[:, 0]
    y = curve[:, 1]
    return x, y


# Lets try it out with some control points
p0 = (0, 0)
p1 = (0.3, 0.5)
p2 = (0.7, 0.2)
p3 = (1, 1)
# Generate the curve and plot it
x, y = bezier_cubic(p0, p1, p2, p3)
plt.plot(x, y)
# Plot the control points on it
x_pt = np.array([p[0] for p in [p0, p1, p2, p3]])
y_pt = np.array([p[1] for p in [p0, p1, p2, p3]])
plt.plot(x_pt, y_pt, "r.--")
plt.axis("equal")
plt.show()
plt.close()

# ----------------------------------------------

# Step 2: Implement a function to compute the area under a curve
# and the length of that curve


def area_under_curve(x: np.array, y: np.array) -> float:
    """Approximage the area under a curve using the trapezoidal rule"""
    dx = np.abs(np.diff(x))
    area = (dx * y[:-1]).sum()
    return area


def length_of_curve(x: np.array, y: np.array) -> float:
    """Approximage the length of a curve using the distance formula"""
    lc = np.sum(np.sqrt((np.diff(x) ** 2) + (np.diff(y) ** 2)))
    return lc


# Lets try it out with (y = 1 - x)
x = np.linspace(0, 1, 1000)
y = 1 - x
plt.plot(x, y, "b")
plt.plot(x, 0 * x, "k--")
plt.plot(0 * x, y, "k--")
plt.axis("equal")
plt.title("y = 1 - x")
plt.show()
plt.close()

# The area w.r.t. the axes is 0.5
area = area_under_curve(x, y)
print(f"Area: {area}")

# Its length is sqrt(2) ~= 1.414
lc = length_of_curve(x, y)
print(f"Length: {lc}")

# ----------------------------------------------

# Step 3: Test functions with some sample control points
v = 0.35
p0 = (1, 0)
p1 = (1, v)
p2 = (v, 1)
p3 = (0, 1)
x, y = bezier_cubic(p0, p1, p2, p3)

area = area_under_curve(x, y)
error = (area - (np.pi / 4)) / (np.pi / 4) * 100
print(f"For v = {v:.2f} the percentage error in area is {error:.2f}%")

l_approx = length_of_curve(x, y)
error = (l_approx - (np.pi / 2)) / (np.pi / 2) * 100
print(f"For v = {v:.2f} the percentage error in length is {error:.2f}%")

plt.figure(figsize=(4, 4))
x_pt = np.array([p[0] for p in [p0, p1, p2, p3]])
y_pt = np.array([p[1] for p in [p0, p1, p2, p3]])
plt.plot(x_pt, y_pt, "r.--")
plt.plot(x, y, "b")
plt.plot(x, 0 * x, "k--")
plt.plot(0 * x, y, "k--")

# Draw an actual quarter circle
t = np.linspace(0, np.pi / 2, 100)
x_circle = np.cos(t)
y_circle = np.sin(t)
plt.plot(x_circle, y_circle, "k-")

plt.axis("equal")
plt.title(f"Cubic Bezier Curve with v = {v}")
plt.show()
plt.close()
