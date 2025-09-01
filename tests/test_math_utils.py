import pytest

from math_utils import add


@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 1, 2), (-1, 1, 0), (100, -7, 93)],
)
def test_add_param(a, b, expected):
    assert add(a, b) == expected


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_with_zero():
    assert add(0, 7) == 7


def test_add(add_origin):
    assert add_origin + add(1, 1) == add(1, 1)
