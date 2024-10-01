import pytest

from solutions.sample import division


@pytest.fixture
def division_data():
    return 12, 3


def test_division(division_data):
    a, b = division_data
    assert division(a, b) == 4
