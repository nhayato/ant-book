__version__ = "0.1.0"


def solve(_: int, job_start: list[int], job_end: list[int]) -> int:
    jobs = [[start, job_end[i]] for i, start in enumerate(job_start)]
    sorted_jobs = sorted(jobs, key=lambda job: job[1])

    ans = 0
    t = 0
    for _, elem in enumerate(sorted_jobs):
        if t < elem[0]:
            ans += 1
            t = elem[1]

    return ans


def main():
    # 出題
    n = 5
    s = [1, 2, 4, 6, 8]
    t = [3, 5, 7, 9, 10]
    print(solve(n, s, t))


if __name__ == "__main__":
    main()
