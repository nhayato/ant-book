from fence_repair import __version__, solve, solve_by_priority_queue


def test_good():
    N = 3
    L = [8, 5, 8]
    assert solve(N, L) == 34


def test_good2():
    N = 5
    L = [3, 4, 5, 1, 2]
    assert solve(N, L) == 33


def test_queue_good():
    N = 3
    L = [8, 5, 8]
    assert solve_by_priority_queue(N, L) == 34


def test_queue_good2():
    N = 5
    L = [3, 4, 5, 1, 2]
    assert solve_by_priority_queue(N, L) == 33


def test_version():
    assert __version__ == "0.1.0"
