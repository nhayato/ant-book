__version__ = "0.1.0"


def solve(N: int, S: str) -> str:
    T = ""

    while S != "":
        rS = S[::-1]
        if S[0] < rS[0]:
            T += S[0]
            S = S[1:]
        else:
            T += S[-1]
            S = S[:-1]

    return T


def main():
    # 出題
    N = 6
    S = "ACDBCB"
    print(solve(N, S))


if __name__ == "__main__":
    main()
