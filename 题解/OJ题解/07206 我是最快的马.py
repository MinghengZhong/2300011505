sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
M = [[0]*11 for _ in range(11)]
m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    M[i][j] = 1

dx = [[2, 2], [-1, 1], [-2, -2], [-1, 1]]
dy = [[-1, 1], [2, 2], [-1, 1], [-2, -2]]
ddx = [1, 0, -1, 0]
ddy = [0, 1, 0, -1]


def bfs():
    c = 0
    q = [(sx, sy)]
    s, e = 0, 1
    f = [[1]*11 for _ in range(11)]
    while s-e:
        c += 1
        for _ in range(s, e):
            x, y = q[_]
            for i in range(4):
                nnx, nny = x+ddx[i], y+ddy[i]
                if 0 <= nnx <= 10 and 0 <= nny <= 10 and M[nnx][nny]:
                    continue
                for j in range(2):
                    nx, ny = x+dx[i][j], y+dy[i][j]
                    if 0 <= nx <= 10 and 0 <= ny <= 10 and M[nx][ny] != 1 and f[nx][ny]:
                        if nx == ex and ny == ey:
                            return c
                        f[nx][ny] = 0
                        q.append((nx, ny))
        s, e = e, len(q)


C = bfs()
l = []


def dfs(x, y, c, f, s):
    global l
    if c == C:
        if x == ex and y == ey:
            l.append(s)
        return
    for i in range(4):
        nnx, nny = x+ddx[i], y+ddy[i]
        if 0 <= nnx <= 10 and 0 <= nny <= 10 and M[nnx][nny]:
            continue
        for j in range(2):
            nx, ny = x+dx[i][j], y+dy[i][j]
            if 0 <= nx <= 10 and 0 <= ny <= 10 and M[nx][ny] != 1 and f[nx][ny]:
                f[nx][ny] = 0
                dfs(nx, ny, c+1, f, s+('-(%d,%d)' % (nx, ny)))
                f[nx][ny] = 1
    return


dfs(sx, sy, 0, [[1]*11 for _ in range(11)], '(%d,%d)' % (sx, sy))
if len(l) == 1:
    print(l[0])
else:
    print(len(l))
