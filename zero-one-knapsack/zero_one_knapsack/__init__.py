__version__ = "0.1.0"
from pprint import pprint


def solve(n: int, elements: list[tuple[int, int]], W: int) -> int:
    # elements[i][0]がweight, elements[i][1]がvalue
    # return rec(0, W, n, elements)

    # dp = [[-1 for i in range(W + 1)] for j in range(len(elements) + 1)]
    # return rec_v2(0, W, n, elements, dp)

    return use_dp_table(n, elements, W)


# i番目以降の品物から重さの総和がj以下になるように選ぶ
def rec(i: int, j: int, n: int, elem: list[tuple[int, int]]) -> int:
    if i == n:
        # 品物はない
        res = 0
    elif j < elem[i][0]:
        # 品物は入らないので次に行く
        res = rec(i + 1, j, n, elem)
    else:
        # 入れない場合と入れる場合をどちらも試す
        res = max(
            rec(i + 1, j, n, elem),
            rec(i + 1, j - elem[i][0], n, elem) + elem[i][1],
        )
    return res


# i番目以降の品物から重さの総和がj以下になるように選ぶ
def rec_v2(
    i: int, j: int, n: int, elem: list[tuple[int, int]], dp: list[list[int]]
) -> int:
    if dp[i][j] >= 0:
        return dp[i][j]
    if i == n:
        # 品物はない
        res = 0
    elif j < elem[i][0]:
        # 品物は入らないので次に行く
        res = rec(i + 1, j, n, elem)
    else:
        # 入れない場合と入れる場合をどちらも試す
        res = max(
            rec(i + 1, j, n, elem),
            rec(i + 1, j - elem[i][0], n, elem) + elem[i][1],
        )
    dp[i][j] = res
    return res


# i番目以降の品物から重さの総和がj以下になるように選んだときの，価値の総和の最大値を示すテーブルを作成
def use_dp_table(n, elements: list[tuple[int, int]], W: int) -> int:
    dp: list[list[int]] = [[0 for i in range(W + 1)] for j in range(len(elements) + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(0, W + 1):
            if j < elements[i][0]:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = max(
                    dp[i + 1][j], dp[i + 1][j - elements[i][0]] + elements[i][1]
                )
    return dp[0][W]


def main():
    n = 4
    elements = [(2, 3), (1, 2), (3, 4), (2, 2)]
    W = 5
    print(solve(n, elements, W))


if __name__ == "__main__":
    main()
