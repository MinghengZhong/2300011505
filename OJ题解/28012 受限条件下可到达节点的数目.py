n = int(input())
g = [set() for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)
f = set(map(int, input().split()))
s, e = 0, 1
v = [1]*n
v[0] = 0
q = [0]
ans = 1
while s-e:
    for i in range(s, e):
        x = q[i]
        for j in g[x]:
            if j not in f and v[j]:
                q.append(j)
                v[j] = 0
                ans += 1
    s, e = e, len(q)
print(ans)
