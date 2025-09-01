import pytest

from math_utils import add


@pytest.fixture
def add_origin():
    """Simple fixture: add(0, 0)."""
    return add(0, 0)


@pytest.fixture
def sample_adds():
    """Set of adds for parametrize/tests."""
    return [add(1, 2), add(3, 4)]
