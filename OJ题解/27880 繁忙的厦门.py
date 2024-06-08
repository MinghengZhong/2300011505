n, m = map(int, input().split())
p = [i for i in range(n+1)]
a, b = 0, 0


def P(x):
    if p[x] != x:
        p[x] = P(p[x])
    return p[x]


for u, v, c in sorted([tuple(map(int, input().split()))for _ in range(m)], key=lambda x: x[2]):
    pu, pv = P(u), P(v)
    if pu-pv:
        p[pu] = pv
        a += 1
        b = c
print(a, b)
