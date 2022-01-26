__version__ = '0.1.0'

# dp table
# --------------
#  j\i a b c d . s[i]
# .  b 0 0 0 0 0
# .  e 0 0 1 1 1
# .  c 0 0 1 1 1
# .  d 0 0 1 2 2
# .    0 0 1 2 3
#   t[j]
def solve(s:str,t:str)->int:
    dp: list[list[int]] = [[0 for i in range(len(s)+1)] for j in range(len(t) + 1)]
    for j in range(len(t)):
        for i in range(len(s)):
            if s[i] == t[j]:
                dp[j+1][i+1] = dp[j][i]+1
            else:
                dp[j+1][i+1] = max(dp[j][i+1],dp[j+1][i])
    return dp[len(t)][len(s)]

def main():
    # 出題
    n = 4
    m = 4
    s = "abcd" # i
    t = "becd" # j
    print(solve(s,t))

if __name__ == "__main__":
    main()