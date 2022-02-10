from heapq import heappop, heappush

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


def solve_by_priority_queue(N: int, L: list[int]) -> int:
    ans = 0
    priority_queue = []
    for i in range(N):
        heappush(priority_queue, L[i])

    while len(priority_queue) > 1:
        # 一番短い板、次に短い板を取り出す
        l1 = heappop(priority_queue)
        l2 = heappop(priority_queue)

        ans += l1 + l2
        heappush(priority_queue, l1 + l2)

    return ans


def main():
    N = 3
    L = [8, 5, 8]
    print(solve(N, L))
    print(solve_by_priority_queue(N, L))


if __name__ == "__main__":
    main()
