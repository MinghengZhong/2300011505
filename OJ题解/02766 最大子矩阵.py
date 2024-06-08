n = int(input())
l = []
while len(l)-n*n:
    l.extend(map(int, input().split()))
M = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        M[i][j] = l[i*n+j]
        if j:
            M[i][j] += M[i][j-1]
ans = -1e9
for i in range(n):
    for j in range(max(i, 1)):
        f = [0]*n
        g = [0]*n
        for k in range(n):
            f[k] = M[k][i]
            if j:
                f[k] -= M[k][j]
            g[k] = f[k]
            if k:
                f[k] += f[k-1]
                g[k] = min(f[k], g[k-1])
        ans = max(ans, f[0])
        for k in range(1, n):
            ans = max(ans, f[k]-g[k-1])
print(ans)
