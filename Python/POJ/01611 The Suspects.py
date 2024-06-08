def P(x):
    if p[x] != x:
        p[x] = P(p[x])
    return p[x]


while 1:
    n, m = map(int, input().split())
    if n == 0:
        break
    p = [i for i in range(n)]
    for _ in range(m):
        l = list(map(int, input().split()))
        x = l[1]
        for y in l[2:]:
            p[P(x)] = p[P(y)] = min(P(x), P(y))
    print(sum(P(i) == 0 for i in range(n)))
