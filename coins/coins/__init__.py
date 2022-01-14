__version__ = "0.1.0"


def solve(
    count_1: int,
    count_5: int,
    count_10: int,
    count_50: int,
    count_100: int,
    count_500: int,
    ans: int,
) -> int:
    counter = 0
    bag = 0

    coins = {
        500: count_500,
        100: count_100,
        50: count_50,
        10: count_10,
        5: count_5,
        1: count_1,
    }

    for k, v in coins.items():
        while v > 0 and bag + k <= ans:
            bag += k
            counter += 1
            v -= 1
    return counter


def main():
    print(solve(3, 2, 1, 3, 0, 2, 620))


if __name__ == "__main__":
    main()
