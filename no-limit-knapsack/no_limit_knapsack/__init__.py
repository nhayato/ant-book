from pprint import pprint

__version__ = "0.1.0"

# O(nW^2)
def solve(n: int, elems: list[tuple[int, int]], W: int) -> int:
    dp: list[list[int]] = [[0 for j in range(W + 1)] for i in range(len(elems) + 1)]

    for i in range(len(elems)):
        for j in range(W + 1):
            k = 0
            weight = elems[i][0]
            value = elems[i][1]
            while k * weight <= j:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - k * weight] + k * value)
                k += 1
    print(dp)
    return dp[n][W]


# O(nW)
def solve_v2(n: int, elems: list[tuple[int, int]], W: int) -> int:
    dp: list[list[int]] = [[0 for j in range(W + 1)] for i in range(len(elems) + 1)]

    for i in range(len(elems)):
        for j in range(W + 1):
            k = 0
            weight = elems[i][0]
            value = elems[i][1]
            if j < weight:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - weight] + value)
    print(dp)
    return dp[n][W]


# use same table
def solve_v3(n: int, elems: list[tuple[int, int]], W: int) -> int:
    dp: list[int] = [0 for j in range(W + 1)]

    for i in range(len(elems)):
        for j in range(elems[i][0], W + 1):
            weight = elems[i][0]
            value = elems[i][1]
            dp[j] = max(dp[j], dp[j - weight] + value)
    print(dp)
    return dp[W]


def main():
    # 出題
    n = 3
    elements = [(3, 4), (4, 5), (2, 3)]  # (w,v)
    W = 7
    print(solve_v3(n, elements, W))


if __name__ == "__main__":
    main()
