import pytest

from solutions.sample import division


@pytest.mark.xfail(reason="Known bug: incorrect division")
def test_known_failure():
    assert division(1, 2) == 1 / 3


@pytest.mark.skip(reason="Not implemented yet")
def test_not_implemented():
    assert division(100, 0) == 0
