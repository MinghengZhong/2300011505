m, n = map(int, input().split())
M = [input() for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(sx, sy, E):
    q = [(sx, sy)]
    p = [[(-1, -1) for j in range(n)] for i in range(m)]
    p[sy][sx] = (-2, -2)
    s, e = 0, 1
    while s-e:
        for i in range(s, e):
            x, y = q[i]
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx < n and 0 <= ny < m and M[y][x] != '1' and p[ny][nx] == (-1, -1):
                    p[ny][nx] = (x, y)
                    if M[ny][nx] == E:
                        return p
                    q.append((nx, ny))
        s, e = e, len(q)


def F(x, y, p):
    l = [(x, y)]
    while p[y][x] != (-2, -2):
        x, y = p[y][x]
        l.append((x, y))
    return l[::-1]


for i in range(m):
    for j in range(n):
        if M[i][j] == 'R':
            p1 = bfs(j, i, 'Y')
        elif M[i][j] == 'Y':
            p2 = bfs(j, i, 'C')
            x1, y1 = j, i
        elif M[i][j] == 'C':
            x2, y2 = j, i
for x, y in F(x1, y1, p1):
    if M[y][x] != 'Y':
        print(y+1, x+1)
for x, y in F(x2, y2, p2):
    print(y+1, x+1)
