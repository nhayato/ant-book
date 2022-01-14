from coins import __version__
from coins import solve


def test_version():
    assert __version__ == "0.1.0"


def test_good():
    assert solve(3, 2, 1, 3, 0, 2, 620) == 6
