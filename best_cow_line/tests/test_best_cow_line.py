from best_cow_line import __version__, solve


def test_version():
    assert __version__ == "0.1.0"


def test_good():
    assert solve(6, "ACDBCB") == "ABCBCD"
