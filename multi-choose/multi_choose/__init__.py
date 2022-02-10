__version__ = '0.1.0'

def solve(n:int, m:int,a:list[int], M:int)->int:
    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1
    for i in range(n):
        for j in range(1,m+1):
            if j -1 -a[i] >= 0:
                dp[i+1][j] = (dp[i+1][j-1] + dp[i][j] - dp[i][j-1-a[i]] + M) % M
            else:
                dp[i+1][j] = (dp[i+1][j-1] + dp[i][j]) % M
    return dp[n][m]

def main():
    n = 3
    m = 3
    a = [1,2,3]
    M = 10000
    print(solve(n,m,a,M))

if __name__ == "__main__":
    main()