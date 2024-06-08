k = 0
while True:
    k += 1
    n, m = map(int, input().split())
    if not m:
        break
    l = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        l[a].append(b)
        l[b].append(a)
    f, ans = [False]*(n+1), 0
    for i in range(1, n+1):
        if not f[i]:
            ans += 1
            L, s, e = [i], 0, 1
            while e-s:
                for j in range(s, e):
                    for a in l[L[j]]:
                        if not f[a]:
                            f[a] = True
                            L.append(a)
                s, e = e, len(L)
    print('Case %d: %d' % (k, ans))
