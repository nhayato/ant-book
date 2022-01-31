from integer_partition import __version__, solve


def test_version():
    assert __version__ == "0.1.0"


def test_dp():
    n = 4
    m = 3
    M = 10000

    assert solve(n, m, M) == 4
