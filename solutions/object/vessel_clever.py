from math import atan2

import matplotlib.pyplot as plt
from vectorfield import VectorField, circular_current
from vessel import Vessel


class VesselClever(Vessel):

    def head_to(self, x: float, y: float, dt: float = 0.05):
        # We want to move in the following direction
        dx = x - self.x
        dy = y - self.y
        theta_goal = atan2(dy, dx)

        # However the vectorfield pushes us
        u, v = self.vectorfield(self.x, self.y)
        theta_field = atan2(v, u)
        diff_theta = theta_goal - theta_field

        # Aim our angle to compesate for the vectorfield
        self.theta += diff_theta
        self.move(dt)


def compute_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def competition(vectorfield: VectorField, dt: float = 0.05):
    x0, y0 = 0, 0
    thrust = 2
    x, y = 2, 2

    ls_vessels = [
        Vessel(vectorfield, x=x0, y=y0, thrust=thrust, theta=0),
        VesselClever(vectorfield, x=x0, y=y0, thrust=thrust, theta=0, color="blue"),
    ]
    ls_dist = [compute_distance(vessel.x, vessel.y, x, y) for vessel in ls_vessels]

    vectorfield.plot([-5, 5, -5, 5])
    plt.scatter(x, y, color="blue")
    # Start an animation to show the movement of the vessel
    # User controls when it stops
    while True:
        for vessel in ls_vessels:
            vessel.head_to(x, y, dt)
            vessel.plot()
        plt.pause(dt)
        if not plt.get_fignums():
            break
        ls_dist = [compute_distance(vessel.x, vessel.y, x, y) for vessel in ls_vessels]
        if any(dist < 0.1 for dist in ls_dist):
            winner: Vessel = ls_vessels[ls_dist.index(min(ls_dist))]
            # Display message on plot
            msg = f"Vessel {winner.color} wins!"
            plt.text(0, 0, msg, fontsize=12, color="black")
            plt.show()
            break


def main():
    vectorfield = VectorField(circular_current)
    competition(vectorfield)


if __name__ == "__main__":
    main()
