__version__ = "0.1.0"


def solve(n: int, a: list[int], m: list[int], K: int) -> bool:
    # return make_bad_dp(n, a, m, K)
    return make_good_dp(n, a, m, K)


def make_good_dp(n: int, a: list[int], m: list[int], K: int) -> bool:
    dp: list[int] = [-1 for i in range(K + 1)]

    dp[0] = 0
    for i in range(n):
        for j in range(K + 1):
            print(dp)
            if dp[j] >= 0:
                dp[j] = m[i]
            elif j < a[i] or dp[j - a[i]] <= 0:
                dp[j] = -1
            else:
                dp[j] = dp[j - a[i]] - 1
    print(dp)
    if dp[K] >= 0:
        return True
    else:
        return False


def make_bad_dp(n: int, a: list[int], m: list[int], K: int) -> bool:
    MAX_N = 100
    MAX_K = 100000
    dp: list[list[bool]] = [[False for i in range(MAX_K + 1)] for j in range(MAX_N + 1)]

    dp[0][0] = True
    for i in range(n):
        for j in range(K + 1):
            k = 0
            while k <= m[i] and k * a[i] <= j:
                dp[i + 1][j] |= dp[i][j - k * a[i]]
                k += 1
    if dp[n][K]:
        return True
    else:
        return False


def main():
    n = 3
    a = [3, 5, 8]
    m = [3, 2, 2]
    K = 17
    print(solve(n, a, m, K))


if __name__ == "__main__":
    main()
