from heapq import heappop, heappush


__version__ = "0.1.0"


def solve(L: int, P: int, N: int, A: list[int], B: list[int]) -> int:
    # ガソリンスタンドを追加
    A.append(L)
    B.append(0)
    N += 1
    print(A)

    heap_queue = []

    # ans: 補給回数, pos: 今いる場所, tank: ガソリン量
    ans = 0
    pos = 0
    tank = P

    for i in range(N):
        # 次にすすむ距離
        d = A[i] - pos

        while tank - d < 0:
            if len(heap_queue) == 0:
                return -1
            tank += heappop(heap_queue) * -1
            ans += 1

        tank -= d
        pos = A[i]
        heappush(heap_queue, B[i] * -1)
    return ans


def main():
    N = 4
    L = 25
    P = 10
    A = [10, 14, 20, 21]
    B = [10, 5, 2, 4]
    print(solve(L, P, N, A, B))


if __name__ == "__main__":
    main()
