__version__ = "0.1.0"
from pprint import pprint


def dfs(y: int, x: int, field: list[list[str]], n: int, m: int):
    # delete W
    if field[y][x] == "W":
        field[y][x] = "."

    # search 8 directions
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx = x + dx
            ny = y + dy

            if 0 <= nx and nx < m and 0 <= ny and ny < n and field[ny][nx] == "W":
                dfs(ny, nx, field, n, m)


def solve(n: int, m: int, field_string: str) -> int:
    counter = 0
    field = [list(line) for line in field_string.splitlines()]
    for i in range(n):
        for j in range(m):
            if field[i][j] == "W":
                dfs(i, j, field, n, m)
                counter += 1
    pprint(field)
    pprint(counter)
    return counter


def main():
    # 出題
    n, m = 10, 12
    field_string = """\
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W."""

    solve(n, m, field_string)


if __name__ == "__main__":
    main()
