T, M = map(int, input().split())
time = [0]*M
value = [0]*M
dp = [0]*(T+1)
for i in range(M):
    time[i], value[i] = map(int, input().split())
for i in range(M):
    for j in range(T, 0, -1):
        if j >= time[i]:
            dp[j] = max(dp[j], dp[j-time[i]]+value[i])
print(dp[-1])
