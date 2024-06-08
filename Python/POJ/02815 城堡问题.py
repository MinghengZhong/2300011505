m = int(input())
n = int(input())
g = [[set() for i in range(n)] for j in range(m)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
for i in range(m):
    l = list(map(int, input().split()))
    for j in range(n):
        for k in range(4):
            if (l[j] >> k) % 2 == 0:
                g[i][j].add((i+dx[k], j+dy[k]))
f = [[1]*n for _ in range(m)]
count = 0
area = 0
for i in range(m):
    for j in range(n):
        if f[i][j]:
            count += 1
            ar = 1
            f[i][j] = 0
            q = [(i, j)]
            s, e = 0, 1
            while s-e:
                for _ in range(s, e):
                    xi, xj = q[_]
                    for ni, nj in g[xi][xj]:
                        if f[ni][nj]:
                            ar += 1
                            f[ni][nj] = 0
                            q.append((ni, nj))
                s, e = e, len(q)
            area = max(ar, area)
print(count)
print(area)
