from bipartite_graph import __version__, Edge, solve


def test_version():
    assert __version__ == "0.1.0"


def test_good():
    n = 3
    g = [Edge(0, 1), Edge(1, 2), Edge(2, 0)]
    assert solve(n, g) == False


def test_good2():
    n = 4
    g = [Edge(0, 1), Edge(0, 3), Edge(1, 2), Edge(2, 3)]
    assert solve(n, g) == True
