__version__ = "0.1.0"
from bisect import bisect_left


def solve_o_n_hat_4(n: int, m: int, k: list[int]) -> bool:
    for x1 in k:
        for x2 in k:
            for x3 in k:
                for x4 in k:
                    if x1 + x2 + x3 + x4 == m:
                        return True

    return False


def solve_o_n_hat_3_log_n(n: int, m: int, k: list[int]) -> bool:
    sorted_list = sorted(k)

    for a in range(n):
        for b in range(n):
            for c in range(n):
                if search(sorted_list, m - k[a] - k[b] - k[c]):
                    return True
    return False


def solve(n: int, m: int, k: list[int]) -> bool:
    pair_list = set()

    # 2種類の組み合わせを作る
    for a in range(n):
        for b in range(n):
            pair_list.add(k[a] + k[b])

    pair_list = list(sorted(pair_list))

    # a, b, c, dではなくa+b, c+d
    for pair in pair_list:
        if search(pair_list, m - pair):
            return True
    return False


def search(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False


def binary_search(sorted_list: list[int], target: int) -> bool:
    # k[l], k[l + 1], ... , k[r-1]
    l = 0
    r = len(sorted_list)

    while r - l >= 1:
        i = int((l + r) / 2)  # どうするのか
        if sorted_list[i] == target:
            return True
        elif sorted_list[i] < target:
            l = i + 1
        else:
            r = i
    return False


def main():
    # 出題
    n = 3
    m = 10
    k = [1, 3, 5]

    if solve(n, m, k):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
