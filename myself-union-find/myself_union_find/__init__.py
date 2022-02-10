__version__ = "0.1.0"


MAX_N = 50000

par = [0 for i in range(MAX_N)]
rank = [0 for i in range(MAX_N)]


def init(n: int):
    for i in range(n):
        par[i] = i
        rank[i] = 0


# 木の根を求める
def find(x: int) -> int:
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


# xとyの属する集合を併合
def unite(x: int, y: int):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


# xとyが同じ集合に属するか否か
def same(x: int, y: int) -> bool:
    return find(x) == find(y)


def solve(N, K, T, X, Y) -> int:
    init(N * 3)

    ans = 0

    # 各情報を精査し、矛盾があったらansに加算する
    for i in range(K):
        t = T[i]
        x = X[i] - 1
        y = Y[i] - 1

        # 正しくない番号（0からN-1の範囲外）
        if not (0 <= x < N and 0 <= y < N):
            ans += 1
            continue

        if t == 1:
            # xとyは同じ種類
            if same(x, y + N) or same(x, y + 2 * N):
                ans += 1
            else:
                unite(x, y)
                unite(x + N, y + N)
                unite(x + N * 2, y + N * 2)
        else:
            # xはyを食べるという情報
            if same(x, y) or same(x, y + 2 * N):
                ans += 1
            else:
                unite(x, y + N)
                unite(x + N, y + 2 * N)
                unite(x + 2 * N, y)

    return ans


def main():
    N = 100
    K = 7
    T = [1, 2, 2, 2, 1, 2, 1]
    X = [101, 1, 2, 3, 1, 3, 5]
    Y = [1, 2, 3, 3, 3, 1, 5]

    print(solve(N, K, T, X, Y))


if __name__ == "__main__":
    main()
