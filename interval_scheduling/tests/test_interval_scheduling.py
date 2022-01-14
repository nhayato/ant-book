from interval_scheduling import __version__, solve


def test_version():
    assert __version__ == "0.1.0"


def test_good():
    assert solve(5, [1, 2, 4, 6, 8], [3, 5, 7, 9, 10]) == 3
