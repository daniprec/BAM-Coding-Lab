from math import atan2

import numpy as np

from solutions.vectorfield import VectorField
from solutions.vectorfield_bam import bam, circular, vf1, vf2, vf3, vf4, vf5, vf6, vf7
from solutions.vessel import Vessel
from solutions.vessel_clever import competition


class VesselRandom(Vessel):
    # Team B
    # defining the inheritance
    def __init__(self, vectorfield, x=0, y=0, thrust=1, theta=0, color="red"):
        super().__init__(vectorfield, x, y, thrust, theta, color)

    def head_to(self, x, y, dt=0.05):
        self.theta = np.random.randint(1, 360)
        # Convert to radians
        u, v = self.vectorfield(self.x, self.y)
        dx = u + self.thrust * np.cos(self.theta)
        dy = v + self.thrust * np.sin(self.theta)
        self.x += dx * dt
        self.y += dy * dt


class VesselAggressive(Vessel):
    # Team B
    def __init__(self, vectorfield, x=0, y=0, thrust=1, theta=0, color="red"):
        super().__init__(vectorfield, x, y, thrust, theta, color)

    def head_to(self, x, y, dt=0.05):
        dx = x - self.x
        # updating the same as the head_to method, distance b/w current position and target x and y
        dy = y - self.y
        distance = np.sqrt(dx**2 + dy**2)
        # calculates how far away the vessel is from the target positions
        if distance > 1:
            self.theta = atan2(dy, dx)
        # when the vessel is far enough away, the theta is updated in the same was as in the head_to method.
        else:
            # when the distance is less than 1, so relatively close to the target point
            self.theta = np.arctan2(dy, dx) + np.pi / 2
        # the theta will be perpendicular to the target direction. takes a detour, avoids the
        # vessel to get closer and closer to the target but never actually reaching it, takes a detour
        self.move(dt)


class VesselGradient(Vessel):
    # Team B
    def __init__(self, vectorfield, x=0, y=0, thrust=1, theta=0, color="red"):
        super().__init__(vectorfield, x, y, thrust, theta, color)

    def head_to(self, x, y, dt=0.05):
        du_dx, dv_dx, du_dy, dv_dy = self.vectorfield.gradient(self.x, self.y)
        # Compute gradient at vessel's current position
        dx_goal = x - self.x
        dy_goal = y - self.y
        theta_goal = np.arctan2(dy_goal, dx_goal)
        # Compute direction from current position to goal point
        theta_gradient = np.arctan2(du_dy, du_dx)
        # Compute direction of gradient at vessel's current position
        self.theta = theta_goal + 0.5 * theta_gradient
        # Update theta to point in direction of gradient relative to goal point, with some
        # weighting towards the goal direction
        self.move(dt)
        # the concept for this was trying to move in the direction of the negative gradient.


class VesselNegativeGradient(Vessel):
    # Team B
    def __init__(self, vectorfield, x=0, y=0, thrust=1, theta=0, color="red"):
        super().__init__(vectorfield, x, y, thrust, theta, color)

    def head_to(self, x, y, dt=0.05):
        du_dx, dv_dx, du_dy, dv_dy = self.vectorfield.gradient(x, y)
        u, v = self.vectorfield(self.x, self.y)
        theta_field = np.arctan2(v, u)
        dx_goal = x - self.x
        dy_goal = y - self.y
        theta_goal = np.arctan2(dy_goal, dx_goal)
        theta_gradient = np.arctan2(-du_dy, -du_dx)
        self.theta = theta_field + np.pi + theta_gradient + theta_goal
        self.move(dt)


class VesselPerpendicular(Vessel):
    # Team B
    def __init__(self, vectorfield, x=0, y=0, thrust=1, theta=0, color="red"):
        super().__init__(vectorfield, x, y, thrust, theta, color)

    def head_to(self, x, y, dt=0.05):
        dx = x - self.x
        dy = y - self.y
        theta_goal = np.arctan2(dy, dx)
        u, v = self.vectorfield(self.x, self.y)
        theta_field = np.arctan2(v, u)
        self.theta = theta_field + np.pi / 2
        # Move perpendicular to the vector field
        self.move(dt)


class VesselProperties(Vessel):
    # Team B
    def __init__(self, vectorfield, x=0, y=0, thrust=1, theta=0, color="red"):
        super().__init__(vectorfield, x, y, thrust, theta, color)
        # we can compare the direction we want to move to with the gradient that we have.

    def head_to(self, x, y, dt=0.05):  # the direction we want to move to:
        dx = x - self.x
        dy = y - self.y
        theta_towards = np.arctan2(dx, dy)
        # the direction of the gradient:
        grad_x, grad_y = self.vectorfield(self.x, self.y)
        theta_gradient = np.arctan2(grad_x, grad_y)
        # we know that the gradient pushes the vessel a lot. but we do not want to move in the direction of the gradient.
        # we can look at the difference between the thetas - one is the one we want to move towards and the other one is the one we are
        # "forced" to move towards.
        theta = theta_towards - theta_gradient
        # we do not want to move in the direction of the vector field. so we add the "theta" to the self.theta so that we minimize our movement
        # with the gradient.
        if abs(theta) > np.pi / 2:
            # If the angle difference is greater than pi/2, move in the opposite direction of the vector field - this is
            # the tip that AI gave me when I fed them the above code in this method.
            self.theta = theta_gradient + np.pi
        else:
            self.theta = theta_towards
        self.move(dt)


class VesselOut(Vessel):
    # Team B
    def __init__(self, vectorfield, x=0, y=0, thrust=1, theta=0, color="red"):
        super().__init__(vectorfield, x, y, thrust, theta, color)

    def head_to(self, x, y, dt=0.05):
        dx = x - self.x
        dy = y - self.y
        theta_towards = np.arctan2(dx, dy)
        grad_x, grad_y = self.vectorfield(self.x, self.y)
        theta_gradient = np.arctan2(grad_x, grad_y)
        self.theta = 0.5 * theta_towards - 2 * theta_gradient
        self.move(dt)


def main():
    x0, y0 = 1, 1
    xgoal, ygoal = -2, -2
    thrust = 2

    dict_vessels = {
        "VesselRandom": "blue",
        "VesselAggressive": "purple",
        "VesselGradient": "orange",
        "VesselNegativeGradient": "yellow",
        "VesselPerpendicular": "pink",
        "VesselProperties": "brown",
        "VesselOut": "teal",
    }

    for fun in [bam, circular, vf1, vf2, vf3, vf4, vf5, vf6, vf7]:
        vf = VectorField(fun)
        ls_vessels = [
            eval(vessel)(vf, x0, y0, thrust, 0, color)
            for vessel, color in dict_vessels.items()
        ]

        competition(ls_vessels, x=xgoal, y=ygoal)


if __name__ == "__main__":
    main()
