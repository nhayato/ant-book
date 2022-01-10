__version__ = "0.1.0"


def dfs(i: int, sum: int, n: int, a: list[int], k: int) -> bool:
    # n個決めて，sumとkの比較
    if i == n:
        return sum == k

    # a[i]を使わない
    if dfs(i + 1, sum, n, a, k):
        return True
    # a[i]を使う
    if dfs(i + 1, sum + a[i], n, a, k):
        return True

    # false
    return False


def solve(n: int, a: list[int], k=int) -> bool:
    return dfs(0, 0, n, a, k)


def main():
    n = 4
    a = [1, 2, 4, 7]
    k = 13

    if solve(n, a, k) is True:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
