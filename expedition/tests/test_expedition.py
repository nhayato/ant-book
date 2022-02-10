from expedition import __version__, solve


def test_version():
    assert __version__ == "0.1.0"


def test_good():
    N = 4
    L = 25
    P = 10
    A = [10, 14, 20, 21]
    B = [10, 5, 2, 4]
    assert solve(L, P, N, A, B) == 2
