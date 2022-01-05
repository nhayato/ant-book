__version__ = "0.1.0"


def solve(list_size: int, edge_list: list[int]) -> int:
    ans = 0

    # i < j < k
    for i in range(0, list_size):
        for j in range(i + 1, list_size):
            for k in range(j + 1, list_size):
                len = edge_list[i] + edge_list[j] + edge_list[k]
                max_edge = max(edge_list[i], max(edge_list[j], edge_list[k]))
                rest = len - max_edge

                if max_edge < rest:
                    ans = max(ans, len)

    return ans


def main():
    # 出題
    n = 5
    a = [2, 3, 4, 5, 10]

    print(solve(n, a))


if __name__ == "__main__":
    main()
