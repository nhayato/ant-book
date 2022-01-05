__version__ = "0.1.0"


def solve(L: int, n: int, x: list[int]):
    # 最小時間
    est_minimum = 0
    for _, elem in enumerate(x):
        est_minimum = max(est_minimum, min(elem, L - elem))

    # 最大時間
    est_maximum = 0
    for _, elem in enumerate(x):
        est_maximum = max(est_maximum, max(elem, L - elem))

    return "{} {}".format(est_minimum, est_maximum)


def main():
    # 出題
    L = 10
    n = 3
    x = [2, 6, 7]

    solve(L, n, x)


if __name__ == "__main__":
    main()
