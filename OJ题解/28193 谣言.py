def P(x):
    if p[x] != x:
        p[x] = P(p[x])
    return p[x]


n, m = map(int, input().split())
l = list(map(int, input().split()))
p = [i for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    pa, pb = P(a), P(b)
    l[pa] = min(l[pa], l[pb])
    l[pb] = min(l[pa], l[pb])
    p[pa] = pb
g = set()
ans = 0
for i in range(n):
    pi = P(i)
    if pi not in g:
        g.add(pi)
        ans += l[pi]
print(ans)
