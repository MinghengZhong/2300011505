d = {}
for _ in range(int(input())):
    s = input()
    d[s] = {}
for _ in range(int(input())):
    a, b, x = input().split()
    d[a][b] = d[b][a] = int(x)
for _ in range(int(input())):
    a, b = input().split()
    if a == b:
        print(a)
        continue
    p = {a: a}
    g = {a: 0}
    l = set((a, e) for e in d[a].keys())
    f = 1
    while f:
        E, X = set(), -1
        for s, e in l:
            x = d[s][e]+g[s]
            if X < 0 or x < X:
                E = {(s, e)}
                X = x
            elif x == X:
                E.add((s, e))
        l -= E
        if not E:
            break
        for s, e in E:
            p[e] = s
            g[e] = X
            if e == b:
                ans = e
                x, y = p[e], e
                while p[y] != y:
                    ans = x+'->(%d)->' % d[x][y]+ans
                    x, y = p[x], x
                print(ans)
                f = 0
                break
            for ee in d[e].keys():
                if not p.get(ee):
                    l.add((e, ee))
