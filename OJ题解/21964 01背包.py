N, M = map(int, input().split())
n = [0]*N
v = [0]*N
dp = [0]*(M+1)
for i in range(N):
    n[i], v[i] = map(int, input().split())
for i in range(N):
    for j in range(M, n[i]-1, -1):
        dp[j] = max(dp[j], dp[j-n[i]]+v[i])
print(dp[-1])
