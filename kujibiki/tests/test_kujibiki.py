import csv

from kujibiki import __version__
from kujibiki import solve


def test_version():
    assert __version__ == "0.1.0"


def test_good():
    assert solve(3, 10, [1, 3, 5]) == True


def test_1000():
    with open("tests/1000.csv") as f:
        reader = csv.reader(f)
        line = [int(enum) for enum in [row for row in reader][0]]
        assert solve(1000, 100000, line) == True
        # 24203 57625 9086 9086
