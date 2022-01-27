from no_limit_knapsack import __version__, solve, solve_v2, solve_v3


def test_version():
    assert __version__ == "0.1.0"


def test_good_solve():
    n = 3
    elements = [(3, 4), (4, 5), (2, 3)]  # (w,v)
    W = 7
    assert solve(n, elements, W) == 10


def test_good_solve2():
    n = 3
    elements = [(3, 4), (4, 5), (2, 3)]  # (w,v)
    W = 7
    assert solve_v2(n, elements, W) == 10


def test_good_solve3():
    n = 3
    elements = [(3, 4), (4, 5), (2, 3)]  # (w,v)
    W = 7
    assert solve_v3(n, elements, W) == 10
