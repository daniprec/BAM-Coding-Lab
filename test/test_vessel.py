from solutions.vectorfield import VectorField
from solutions.vessel import Vessel


def vectorfield_zero(x: float, y: float) -> tuple:
    """
    Simple vector field function that returns 0.
    """
    return 0, 0


def test_vectorfield_zero():
    """
    Test the Vessel class without a vector field.
    """
    vf = VectorField(vectorfield_zero)
    vessel = Vessel(vf)
    # Move the vessel
    vessel.move(dt=1)
    assert vessel.x == 0
    assert vessel.y == 0


def vectorfield_ones(x: float, y: float) -> tuple:
    """
    Simple vector field function that returns 1.
    """
    return 1, 1


def test_vectorfield_ones():
    """
    Test the Vessel class with a vector field that returns 1.
    """
    vf = VectorField(vectorfield_ones)
    vessel = Vessel(vf)
    # Move the vessel
    for _ in range(10):
        vessel.move(dt=0.1)
    # Assert values are close enough to 1
    assert abs(vessel.x - 1) < 1e-5
    assert abs(vessel.y - 1) < 1e-5
