n, a, b, c = map(int, input().split())
l = []
if a <= n and a not in l:
    l.append(a)
if b <= n and b not in l:
    l.append(b)
if c <= n and c not in l:
    l.append(c)
dp = [0]*(n+1)
for j in l:
    dp[j] = 1
for i in range(min(l)+1, n+1):
    for j in l:
        if i >= j and dp[i-j] != 0:
            dp[i] = max(dp[i], dp[i-j]+1)
print(dp[-1])
