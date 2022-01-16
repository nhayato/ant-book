from zero_one_knapsack import __version__, solve


def test_version():
    assert __version__ == "0.1.0"


def test_good():
    assert solve(4, [(2, 3), (1, 2), (3, 4), (2, 2)], 5) == 7
