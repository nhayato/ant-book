from longest_common_subsequence_problem import __version__, solve


def test_version():
    assert __version__ == '0.1.0'

def test_good():
    n = 4
    m = 4
    s = "abcd" # i
    t = "becd" # j
    assert solve(s,t) == 3

def test_good2():
    n = 4
    m = 5
    s = "abcd" # i
    t = "becdf" # j
    assert solve(s,t) == 3