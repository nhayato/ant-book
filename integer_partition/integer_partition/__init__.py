__version__ = "0.1.0"


def solve(n: int, m: int, M: int) -> int:
    dp: list[list[int]] = [[0 for i in range(n + 1)] for j in range(m + 1)]
    dp[0][0] = 1
    for i in range(1, m + 1):
        for j in range(n + 1):
            if j - i >= 0:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - i]) % M
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]


def main():
    n = 4
    m = 3
    M = 10000
    print(solve(n, m, M))


if __name__ == "__main__":
    main()
