__version__ = "0.1.0"


import sys


def solve(n: int, a: list[int]) -> int:
    return first_dp(n, a)


# dp[i]: 最後がa_iであるような最長の増加部分列の長さ
def first_dp(n: int, a: list[int]) -> int:
    dp: list[int] = [-1 for i in range(n)]
    ans = 0

    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        ans = max(ans, dp[i])
    return ans


def main():
    n = 5
    a = [4, 2, 3, 1, 5]
    print(solve(n, a))


if __name__ == "__main__":
    main()
