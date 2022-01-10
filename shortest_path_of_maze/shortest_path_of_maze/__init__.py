__version__ = "0.1.0"
from pprint import pprint
from collections import deque


def solve(n: int, m: int, maze: str) -> int:
    INF = -1
    goal: list[int] = [-1, -1]
    field = [list(line) for line in maze.splitlines()]
    queue: deque[list[int]] = deque([])
    route: list[list[int]] = [[INF for _ in range(m)] for _ in range(n)]

    vec_x = [1, 0, -1, 0]
    vec_y = [0, 1, 0, -1]
    for dy, line in enumerate(field):
        for dx, elem in enumerate(line):
            if elem == "S":
                queue.append([dx, dy])  # start
                route[dy][dx] = 0
            elif elem == "G":
                print("goal", dx, dy)
                goal = [dx, dy]
    while queue:
        target_x, target_y = queue.popleft()
        if [target_x, target_y] == goal:
            break
        for i in range(4):
            ny = target_y + vec_y[i]
            nx = target_x + vec_x[i]
            if (
                0 <= nx
                and nx < m
                and 0 <= ny
                and ny < n
                and field[ny][nx] != "#"
                and route[ny][nx] == INF
            ):
                queue.append([nx, ny])
                route[ny][nx] = route[target_y][target_x] + 1
    return route[goal[1]][goal[0]]


def main():
    # 出題
    n = 10  # 縦（y）
    m = 10  # 横（x）
    maze = """\
#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#"""
    print(solve(n, m, maze))


if __name__ == "__main__":
    main()
