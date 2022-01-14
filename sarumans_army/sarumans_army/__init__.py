__version__ = "0.1.0"


def solve(N: int, R: int, X: list[int]) -> int:
    counter = 0
    r_range = X[0] + R
    for i in range(1, len(X)):
        if X[i] <= r_range:
            continue
        elif X[i] > r_range:
            counter += 1
            r_range = X[i] + R

    return counter


def main():
    # 出題
    N = 6
    R = 10
    X = [1, 7, 15, 20, 30, 50]

    print(solve(N, R, X))


if __name__ == "__main__":
    main()
