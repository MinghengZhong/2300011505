while True:
    n, m = map(int, input().split())
    if m == n == 0:
        break
    M = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        s = input().split()
        for j in range(m):
            if s[j] == '1':
                M[i][j] = M[i][j+1] = M[i+1][j] = M[i+1][j+1] = 1
    s = input().split()
    x, y, a, b = map(int, s[:4])
    f = ('east', 'south', 'west', 'north').index(s[4])
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    def bfs(x, y, a, b, f):
        if x == a and y == b:
            return 0
        if x <= 0 or x >= n or y <= 0 or y >= m or M[x][y]:
            return -1
        if a <= 0 or a >= n or b <= 0 or b >= m or M[a][b]:
            return -1
        s, e = 0, 1
        l = [(x, y, f)]
        g = {(x, y, f)}
        c = 0
        while s != e:
            c += 1
            for i in range(s, e):
                x, y, f = l[i]
                for j in (1, 2, 3):
                    nx, ny = x+j*dx[f], y+j*dy[f]
                    if nx <= 0 or nx >= n or ny <= 0 or ny >= m or M[nx][ny]:
                        break
                    if nx == a and ny == b:
                        return c
                    if (nx, ny, f) not in g:
                        l.append((nx, ny, f))
                        g.add((nx, ny, f))
                for j in (-1, 1):
                    nf = (f+j) % 4
                    if (x, y, nf) not in g:
                        l.append((x, y, nf))
                        g.add((x, y, nf))
            s, e = e, len(l)
        return -1
    print(bfs(x, y, a, b, f))
