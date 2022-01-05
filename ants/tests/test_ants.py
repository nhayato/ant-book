from ants import __version__
from ants import solve


def test_version():
    assert __version__ == "0.1.0"


def test_good():
    assert solve(10, 3, [2, 6, 7]) == "4 8"
