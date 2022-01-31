from longest_increasing_subsequence import __version__, first_dp


def test_version():
    assert __version__ == "0.1.0"


def test_first_dp():
    n = 5
    a = [4, 2, 3, 1, 5]
    first_dp(n, a)
