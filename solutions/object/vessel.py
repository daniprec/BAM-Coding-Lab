from math import atan2, cos, sin

import matplotlib.pyplot as plt
from vectorfield import VectorField, circular_current


class Vessel:
    def __init__(
        self,
        vectorfield: VectorField,
        x: float = 0,
        y: float = 0,
        thrust: float = 0,
        theta: float = 0,
    ):
        self.vectorfield = vectorfield
        self.x = x
        self.y = y
        self.thrust = thrust
        self.theta = theta
        # Hidden attributes to store the plot of the vessel
        self._plot_point = None

    @property
    def thrust_x(self) -> float:
        """
        This property returns the x-component of the thrust vector.
        A property does not need to be called as a method, but as an attribute.
        """
        return self.thrust * cos(self.theta)

    @property
    def thrust_y(self) -> float:
        """
        This property returns the y-component of the thrust vector.
        A property does not need to be called as a method, but as an attribute.
        """
        return self.thrust * sin(self.theta)

    def drift(self, dt: float = 0.05):
        """This method computes the drift of the vessel over a given time interval."""
        # Use finite difference to compute the drift
        u, v = self.vectorfield(self.x, self.y)
        self.x += u * dt
        self.y += v * dt

    def move(self, dt: float = 0.05):
        """This method moves the vessel in the direction of its heading."""
        u, v = self.vectorfield(self.x, self.y)
        dx = u + self.thrust_x
        dy = v + self.thrust_y
        self.x += dx * dt
        self.y += dy * dt

    def head_to(self, x: float, y: float, dt: float = 0.05):
        """This method moves the vessel to a given position."""
        dx = x - self.x
        dy = y - self.y
        self.theta = atan2(dy, dx)
        self.move(dt)

    def plot(self):
        # Remove the previous plot if it exists
        if self._plot_point:
            self._plot_point.remove()
            self._plot_arrow.remove()
        # Plot the vessel at its current heading
        self._plot_point = plt.scatter(self.x, self.y, color="red")
        self._plot_arrow = plt.arrow(
            self.x,
            self.y,
            self.thrust_x / 2,
            self.thrust_y / 2,
            color="red",
            head_width=self.thrust / 10,
        )


def test_drift(vectorfield: VectorField, dt: float = 0.05):
    vessel = Vessel(vectorfield, x=2, y=2)
    vectorfield.plot([-5, 5, -5, 5])
    # Start an animation to show the drift of the vessel
    # User controls when it stops
    while True:
        vessel.drift(dt)
        vessel.plot()
        plt.pause(dt)
        if not plt.get_fignums():
            break


def test_drift_multiple(vectorfield: VectorField, dt: float = 0.05):
    ls_vessels: list[Vessel] = []

    for x in range(4):
        for y in range(4):
            ls_vessels.append(Vessel(vectorfield, x=x, y=y))

    vectorfield.plot([-5, 5, -5, 5])
    # Start an animation to show the movement of the vessel
    # User controls when it stops
    while True:
        for vessel in ls_vessels:
            vessel.drift(dt)
            vessel.plot()
        plt.pause(dt)
        if not plt.get_fignums():
            break


def test_move(vectorfield: VectorField, dt: float = 0.05):
    vessel = Vessel(vectorfield, x=2, y=2, thrust=2, theta=0)
    vectorfield.plot([-5, 5, -5, 5])
    # Start an animation to show the movement of the vessel
    # User controls when it stops
    while True:
        vessel.move(dt)
        vessel.plot()
        plt.pause(dt)
        if not plt.get_fignums():
            break


def test_head_to(vectorfield: VectorField, dt: float = 0.05):
    vessel = Vessel(vectorfield, x=2, y=2, thrust=2, theta=0)
    x, y = -2, -2
    vectorfield.plot([-5, 5, -5, 5])
    plt.scatter(x, y, color="blue")
    # Start an animation to show the movement of the vessel
    # User controls when it stops
    while True:
        vessel.head_to(x, y, dt)
        vessel.plot()
        plt.pause(dt)
        if not plt.get_fignums():
            break


def main():
    vectorfield = VectorField(circular_current)
    test_drift(vectorfield)
    test_drift_multiple(vectorfield)
    test_move(vectorfield)
    test_head_to(vectorfield)


if __name__ == "__main__":
    main()
