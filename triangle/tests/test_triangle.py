from triangle import __version__
from triangle import solve


def test_version():
    assert __version__ == "0.1.0"


def test_goodcase():
    assert solve(5, [2, 3, 4, 5, 10]) == 12


def test_badcase():
    assert solve(4, [4, 5, 10, 20]) == 0
