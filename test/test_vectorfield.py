from solutions.vectorfield import VectorField


def vectorfield_exponetial(x: float, y: float) -> tuple:
    """
    Simple vector field function that returns the square of the input values.
    """
    u = x**2
    v = y**2
    return u, v


def test_vectorfield():
    """
    Test the VectorField class with the vf_exponetial function.
    """
    vf = VectorField(vectorfield_exponetial)
    assert vf(1, 2) == (1, 4)
    assert vf(-2, -3) == (4, 9)
    assert vf(3, 4) == (9, 16)
