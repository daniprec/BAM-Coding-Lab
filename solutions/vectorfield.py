from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np


def horizontal_current(x: float, y: float, strength: float = 1) -> Tuple[float, float]:
    """This function returns the velocity field of a horizontal current at a given point.

    Parameters
    ----------
    x : float
        Position in the x-direction
    y : float
        Position in the y-direction

    Returns
    -------
    Tuple[float, float]
        The velocity field at the given point
    """
    u = -x * strength
    v = 0
    return u, v


def circular_current(x: float, y: float, strength: float = 1) -> Tuple[float, float]:
    """This function returns the velocity field of a circular current at a given point.

    Parameters
    ----------
    x : float
        Position in the x-direction
    y : float
        Position in the y-direction

    Returns
    -------
    Tuple[float, float]
        The velocity field at the given point
    """
    u = -y * strength
    v = x * strength
    return u, v


class VectorField:

    def __init__(self, function: callable, **kwargs):
        self.function = function
        self.kwargs = kwargs

    def __call__(self, x: float, y: float) -> Tuple[float, float]:
        """This method returns the velocity field of the vector field at a given point.

        Parameters
        ----------
        x : float
            Position in the x-direction
        y : float
            Position in the y-direction

        Returns
        -------
        Tuple[float, float]
            The velocity field at the given point
        """
        return self.function(x, y, **self.kwargs)

    def dx(self, x: float, y: float) -> Tuple[float, float]:
        """This method computes the derivate of the x-component of the vector field.
        Uses finite difference method.

        Parameters
        ----------
        x : float
            Position in the x-direction
        y : float
            Position in the y-direction

        Returns
        -------
        Tuple[float, float]
            The derivated velocity field at the given point
        """
        delta = 1e-6
        f = self(x, y)
        fd = self(x + delta, y)
        dudx = (fd[0] - f[0]) / delta
        dvdx = (fd[1] - f[1]) / delta
        return dudx, dvdx

    def dy(self, x: float, y: float) -> Tuple[float, float]:
        """This method computes the derivate of the y-component of the vector field.
        Uses finite difference method.

        Parameters
        ----------
        x : float
            Position in the x-direction
        y : float
            Position in the y-direction

        Returns
        -------
        Tuple[float, float]
            The derivated velocity field at the given point
        """
        delta = 1e-6
        f = self(x, y)
        fd = self(x, y + delta)
        dudy = (fd[0] - f[0]) / delta
        dvdy = (fd[1] - f[1]) / delta
        return dudy, dvdy

    def plot(self, bounds: Tuple[int, int, int, int], step: float = 0.5):
        """This method plots the vector field.

        Parameters
        ----------
        bounds : Tuple[int, int, int, int]
            The bounds of the plot (xmin, xmax, ymin, ymax)
        step : float
            The step size for the grid, default is 0.1
        """

        xmin, xmax, ymin, ymax = bounds
        x = np.arange(xmin, xmax, step)
        y = np.arange(ymin, ymax, step)
        mat_x, mat_y = np.meshgrid(x, y)
        mat_u, mat_v = self(mat_x, mat_y)

        plt.quiver(mat_x, mat_y, mat_u, mat_v)
        # Make it square
        plt.gca().set_aspect("equal", adjustable="box")


def test_call(vf: VectorField):
    print("\n---\nTest call method:")
    ls_pts = [(1, 0), (0, 1), (1, 1)]
    for x, y in ls_pts:
        u, v = vf(x, y)
        print(f"({x}, {y}) -> ({u:.2f}, {v:.2f})")
    print("---\n")


def test_plot(vf: VectorField):
    print("\n---\nTest plot method:")
    vf.plot((-5, 5, -5, 5), step=0.5)
    plt.show()
    print("---\n")


def main():
    print("Testing the VectorField class with horizontal:")
    vf_h = VectorField(horizontal_current, strength=1)
    test_call(vf_h)
    test_plot(vf_h)

    print("Testing the VectorField class with circular:")
    vf_c = VectorField(circular_current, strength=1)
    test_call(vf_c)
    test_plot(vf_c)


if __name__ == "__main__":
    main()
