import re

import pytest

from solutions.sample import division


def test_division():
    assert division(1, 2) == 0.5
    print("Great!")


def test_division_by_zero():
    """
    pytest.raises allows us to check if a function raises an exception
    """
    with pytest.raises(ZeroDivisionError):
        division(1, 0)


def test_type_error():
    """
    The match argument allows us to check the exception message

    re.escape is used to escape special characters in the message
    """
    with pytest.raises(
        TypeError, match=re.escape("unsupported operand type(s) for /: 'int' and 'str'")
    ):
        division(0, "1")
