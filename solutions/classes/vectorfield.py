from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np


class VectorField:

    def __init__(self, strength: int):
        self.strength = strength

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
        u = -self.strength * y
        v = self.strength * x
        return u, v

    def plot(self, bounds: Tuple[int, int, int, int], step: float = 0.1):
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
        plt.show()


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
    print("---\n")


def main():
    vf = VectorField(1)
    test_call(vf)
    test_plot(vf)


if __name__ == "__main__":
    main()
