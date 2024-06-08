def dfs(a):
    global g, f
    f[a] = 0
    S = list(g[a])
    for s in S:
        g[a] |= g[s]
        if f[s]:
            dfs(s)
    return


n, m = map(int, input().split())
g = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[b] |= {a}
    f = [1]*(n+1)
    for j in range(1, n+1):
        if f[j]:
            dfs(j)
ans = []
s = set()
while len(ans)-n:
    for i in range(1, n+1):
        if i not in s:
            g[i] -= s
            if not g[i]:
                s.add(i)
                ans.append('v%d' % i)
                break
print(*ans)
