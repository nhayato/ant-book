from quantity_limit_partial_sum import __version__, make_good_dp


def test_version():
    assert __version__ == '0.1.0'

def test_good_dp():
    n = 3
    a = [3, 5, 8]
    m = [3, 2, 2]
    K = 17
    assert make_good_dp(n, a, m, K) == True