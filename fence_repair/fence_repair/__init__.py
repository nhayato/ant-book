__version__ = "0.1.0"


def solve(N: int, L: list[int]) -> int:
    ans = 0
    for _ in range(N - 1):
        L = sorted(L)
        t = L[0] + L[1]
        ans += t

        L = L[1:]
        if len(L) > 1:
            L[0] = t

    return ans


def main():
    N = 3
    L = [8, 5, 8]
    print(solve(N, L))


if __name__ == "__main__":
    main()
