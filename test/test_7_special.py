import pytest

from solutions.sample import division


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (-6, 2, -3),
        (5, -2, -2.5),
    ],
)
def test_division(a, b, expected):
    """
    Test for valid division cases with various combinations of positive and negative numbers
    """
    assert division(a, b) == expected


@pytest.mark.special
@pytest.mark.parametrize("a, b", [(10, 0), (0, 0)])
def test_divide_by_zero(a, b):
    """
    Test that a ZeroDivisionError is raised when dividing by zero
    """
    with pytest.raises(ZeroDivisionError):
        division(a, b)
