__version__ = "0.1.0"


class Edge:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __str__(self) -> str:
        return f"{self.start} {self.end}"

    def __repr__(self) -> str:
        return f"({self.start} {self.end})"

    def has_v(self, v):
        if self.start == v or self.end == v:
            return True
        else:
            return False

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end


def dfs(v: int, c: int, color: list[int], n: int, g):
    color[v] = c
    for i in range(n):
        # 隣接頂点かの洗い出し
        if not g[i].has_v(v):
            continue

        # 隣接している頂点が同じ色ならFalse
        if g[i].start == v:
            if color[g[i].end] == c:
                return False
        if g[i].end == v:
            if color[g[i].start] == c:
                return False

        # 隣接している頂点がまだ塗られていないなら、-cで塗る
        if g[i].start == v:
            if color[g[i].end] == 0 and not dfs(g[i].end, -c, color, n, g):
                return False
        if g[i].end == v:
            if color[g[i].start] == 0 and not dfs(g[i].start, -c, color, n, g):
                return False

    return True


def solve(n: int, g: list[Edge]) -> bool:
    color_list = [0 for _ in range(n)]  # default:0, color: -1 or 1
    for i in range(n):
        if color_list[i] == 0:
            # まだ頂点iが塗られていなければ1で塗る
            if not dfs(i, 1, color_list, n, g):
                print(color_list)
                return False
    return True


def main():
    n = 3
    g = [Edge(0, 1), Edge(1, 2), Edge(2, 0)]
    print(solve(n, g))

    n = 4
    g = [Edge(0, 1), Edge(0, 3), Edge(1, 2), Edge(2, 3)]
    print(solve(n, g))


if __name__ == "__main__":
    main()
