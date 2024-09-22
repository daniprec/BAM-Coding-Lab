from typing import Tuple

import matplotlib.pyplot as plt
from vectorfield import VectorField, circular_current


class Vessel:
    def __init__(self, vectorfield: VectorField):
        self.vectorfield = vectorfield

    def drift(
        self, x: float, y: float, dt: float, step: int = 10
    ) -> Tuple[float, float]:
        """This method computes the drift of the vessel over a given time interval."""
        u, v = self.vectorfield(x, y)
        # Use finite difference to compute the drift
        for _ in range(step):
            u, v = self.vectorfield(x, y)
            x += u * dt / step
            y += v * dt / step
        return x, y


def test_drift(vessel: Vessel):
    vessel.vectorfield.plot([-5, 5, -5, 5])
    x, y = -2, 2
    dt = 0.05
    pt = plt.scatter(x, y, color="red")
    # Start an animation to show the drift of the vessel
    # User controls when it stops
    while True:
        x, y = vessel.drift(x, y, dt)
        pt.set_offsets([x, y])
        plt.pause(0.1)
        if not plt.get_fignums():
            break


def main():
    vectorfield = VectorField(circular_current)
    vessel = Vessel(vectorfield)
    test_drift(vessel)


if __name__ == "__main__":
    main()
