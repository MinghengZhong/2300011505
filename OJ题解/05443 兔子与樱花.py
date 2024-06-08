import heapq


def dijkstra(g, s, e):
    d = {v: -1 for v in g}
    d[s] = 0
    h = [(0, s)]
    p = {v: None for v in g}
    while h:
        X, V = heapq.heappop(h)
        if X > d[V] and d[V] > 0:
            continue
        for n, w in g[V].items():
            x = X + w
            if x < d[n] or d[n] < 0:
                d[n] = x
                p[n] = V
                heapq.heappush(h, (x, n))
    path = []
    if p[e] is not None:
        v = e
        while v is not None:
            path.append(v)
            v = p[v]
    return path[::-1]


P = set()
for _ in range(int(input())):
    P.add(input())
g = {p: {} for p in P}
for _ in range(int(input())):
    a, b, x = input().split()
    g[a][b] = g[b][a] = int(x)
for _ in range(int(input())):
    a, b = input().split()
    if a == b:
        print(a)
        continue
    path = dijkstra(g, a, b)
    ans = ''
    for i in range(len(path)-1):
        ans += path[i]+'->(%d)->' % g[path[i]][path[i+1]]
    print(ans+path[-1])
