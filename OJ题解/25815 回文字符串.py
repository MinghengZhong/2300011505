s = input()
n = len(s)
dp = [[0]*n for _ in range(n)]
for k in range(1, n):
    for i in range(n-k):
        j = i+k
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1]
        else:
            dp[i][j] = min(dp[i+1][j], dp[i][j-1], dp[i+1][j-1])+1
print(dp[0][n-1])
