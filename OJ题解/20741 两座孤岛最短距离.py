g = set()
l = []
c = -1
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)


def bfs(M, n, K):
    global g, l, c
    s, e = 0, len(l)
    while s != e:
        c += K
        for k in range(s, e):
            for _ in range(4):
                x, y = l[k][0]+dx[_], l[k][1]+dy[_]
                if 0 <= x < n and 0 <= y < n and (M[x][y] or K) and (x, y) not in g:
                    g.add((x, y))
                    l.append((x, y))
                    if K and M[x][y]:
                        return
        s, e = e, len(l)


n = int(input())
M = [list(map(int, input())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if M[i][j]:
            g.add((i, j))
            l.append((i, j))
            bfs(M, n, 0)
            break
    if g:
        break
bfs(M, n, 1)
print(c)
