m, n = map(int, input().split())
l = []
g = [set() for _ in range(m)]
f = [0]*m
S = []
for _ in range(n):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)
    l.append(a)
S = set()
a, b = 'yes', 'no'
for i in range(m):
    if not f[i]:
        f[i] = 1
        if S:
            a = 'no'
        S = set([i])
        L = [i]
        s, e = 0, 1
        while s != e:
            for j in range(s, e):
                for k in g[L[j]]:
                    if not f[k]:
                        f[k] = 1
                        L.append(k)
                        S.add(k)
            s, e = e, len(L)
        c = sum(j in S for j in l)
        if c >= len(S):
            b = 'yes'
print('connected:%s\nloop:%s' % (a, b))
