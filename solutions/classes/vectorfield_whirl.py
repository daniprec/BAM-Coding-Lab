from typing import Tuple

from vectorfield import VectorField, test_call, test_plot


class VectorFieldWhirl(VectorField):
    def __init__(self, strength: float):
        """This class represents a vector field with a whirl component.

        Parameters
        ----------
        strength : float
            The strength of the vector field
        whirl : float
            The strength of the whirl component
        """
        super().__init__(strength)

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
        u = self.strength * (-y + x)
        v = self.strength * (x + y)
        return u, v


def main():
    vf = VectorFieldWhirl(1)
    test_call(vf)
    test_plot(vf)


if __name__ == "__main__":
    main()
