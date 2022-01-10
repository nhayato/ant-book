from subset_num_problem import __version__
from subset_num_problem import solve


def test_version():
    assert __version__ == "0.1.0"


def test_good():
    n = 4
    a = [1, 2, 4, 7]
    k = 13
    assert solve(n, a, k) == True


def test_bad():
    n = 4
    a = [1, 2, 4, 7]
    k = 15
    assert solve(n, a, k) == False
