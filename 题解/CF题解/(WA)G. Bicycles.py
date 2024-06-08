t = int(input())
ans = [0]*t
for _ in range(t):
    n, m = map(int, input().split())
    next = [set() for i in range(n+1)]
    W = [[0]*(n+1) for i in range(n+1)]
    gone = [False]*(n+1)
    gone[1] = True
    for i in range(m):
        u, v, w = map(int, input().split())
        next[u].add(v)
        next[v].add(u)
        if W[u][v] == 0:
            W[u][v], W[v][u] = w, w
        else:
            W[u][v], W[v][u] = min(w, W[u][v]), min(w, W[v][u])
    s = [0]+list(map(int, input().split()))
    l = [(1, s[1], 0)]
    mintime = [0]*(n+1)
    mins = [0]*(n+1)
    mins[1] = s[1]
    start, end = 0, 0
    while end != len(l):
        start, end = end, len(l)
        for i in range(start, end):
            now, lasts, time = l[i]
            for j in next[now]:
                if not gone[j]:
                    gone[j] = True
                    mintime[j] = time+W[now][j]*lasts
                    mins[j] = min(lasts, s[j])
                    l.append((j, mins[j], mintime[j]))
                elif time+W[now][j]*lasts < mintime[j]:
                    mintime[j] = time+W[now][j]*lasts
                    mins[j] = min(lasts, mins[j])
                    l.append((j, min(lasts, s[j]), mintime[j]))
                elif lasts < mins[j]:
                    mins[j] = lasts
                    l.append((j, mins[j], time+W[now][j]*lasts))
    ans[_] = mintime[n]
for a in ans:
    print(a)
