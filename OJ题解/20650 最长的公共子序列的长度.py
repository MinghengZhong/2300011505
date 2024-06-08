a, b = input(), input()
m, n = len(a), len(b)
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(m):
    for j in range(n):
        if a[i] == b[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
print(dp[m][n])
