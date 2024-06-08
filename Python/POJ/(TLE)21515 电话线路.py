from heapq import heappop as O, heappush as I
from copy import deepcopy as C
n, p, k = map(int, input().split())
g = {i+1: set() for i in range(n)}
w = [[-1]*(n+1) for _ in range(n+1)]
for _ in range(p):
    a, b, l = map(int, input().split())
    g[a].add(b)
    g[b].add(a)
    w[a][b] = w[b][a] = l


def bfs():
    c = 0
    s, e = 0, 1
    q = [1]
    f = [1]*(n+1)
    f[1] = 0
    while s-e:
        c += 1
        for i in range(s, e):
            x = q[i]
            for y in g[x]:
                if f[y]:
                    if y == n:
                        return c
                    f[y] = 0
                    q.append(y)
        s, e = e, len(q)
    return -1


c = bfs()
if c <= k:
    print(min(c, 0))
    exit()
ans = 1e9


def dfs(x, B, S, f):
    global ans
    if x == n:
        ans = -S[0]
        return
    for y in g[x]:
        if f[y]:
            hb = C(B)
            hs = C(S)
            W = w[x][y]
            if len(hb)-k:
                I(hb, W)
            else:
                I(hb, W)
                I(hs, -O(hb))
            if hs and -hs[0] >= ans:
                continue
            f[y] = 0
            dfs(y, hb, hs, f)
            f[y] = 1
    return


dfs(1, [], [], [1]*(n+1))
print(ans)
