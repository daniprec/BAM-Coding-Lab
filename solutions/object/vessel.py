import matplotlib.pyplot as plt
from vectorfield import VectorField, circular_current


class Vessel:
    def __init__(
        self,
        vectorfield: VectorField,
        x: float = 0,
        y: float = 0,
        speed: float = 0,
        theta: float = 0,
    ):
        self.vectorfield = vectorfield
        self.x = x
        self.y = y
        self.speed = speed
        self.theta = theta

    def drift(self, dt: float):
        """This method computes the drift of the vessel over a given time interval."""
        # Use finite difference to compute the drift
        u, v = self.vectorfield(self.x, self.y)
        self.x += u * dt
        self.y += v * dt


def test_drift(vessel: Vessel):
    vessel.vectorfield.plot([-5, 5, -5, 5])
    dt = 0.05
    pt = plt.scatter(vessel.x, vessel.y, color="red")
    # Start an animation to show the drift of the vessel
    # User controls when it stops
    while True:
        vessel.drift(dt)
        pt.set_offsets([vessel.x, vessel.y])
        plt.pause(0.1)
        if not plt.get_fignums():
            break


def main():
    vectorfield = VectorField(circular_current)
    vessel = Vessel(vectorfield, x=2, y=2, speed=1, theta=0)
    test_drift(vessel)


if __name__ == "__main__":
    main()
