import numpy as np


def bezier(ls_pts: list[tuple], t: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate a cubic Bézier curve with four control points
    This function ONLY works for four control points.
    Your task is to implement a function that generates a Bézier curve
    for any number of control points.
    """
    # Extract the points from the list
    assert len(ls_pts) == 4, "This function only works for four control points"
    p0, p1, p2, p3 = ls_pts
    # Ensure t is the appropiate shape
    t = t.reshape(-1, 1)
    # Generate the curve
    curve = (
        (np.power(1 - t, 3) * p0)
        + (3 * np.power(1 - t, 2) * t * p1)
        + (3 * (1 - t) * np.power(t, 2) * p2)
        + (np.power(t, 3) * p3)
    )
    x = curve[:, 0]
    y = curve[:, 1]
    return x, y


def test_bezier():
    """
    Test the bezier function.
    To try this out, run the script in the command line!
    $ python code/bezier.py
    """
    ls_pts = [(1, 0), (1, 0.3), (0.3, 1), (0, 1)]
    t = np.array([0, 0.5, 0.75, 1])
    x, y = bezier(ls_pts, t)
    x_expected = np.array([1.0, 0.6125, 0.2828125, 0.0])
    y_expected = np.array([0.0, 0.6125, 0.8859375, 1.0])

    if not np.allclose(x, x_expected):
        print(f"Expected x: {x_expected}, but got {x}")
    elif not np.allclose(y, y_expected):
        print(f"Expected y: {y_expected}, but got {y}")
    else:
        print("All tests passed!")


if __name__ == "__main__":
    # When running the script from the command line,
    # the test will be executed.
    test_bezier()
