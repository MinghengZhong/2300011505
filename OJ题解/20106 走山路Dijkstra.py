dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def bfs(l, a, b):
    global M, ans
    while True:
        N = set()
        S = set()
        c = -1
        for x, y in l:
            f = 1
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if M[nx][ny] != '#' and ans[nx][ny] == -1:
                    f = 0
                    newans = ans[x][y] + abs(int(M[x][y])-int(M[nx][ny]))
                    if c == -1 or newans < c:
                        c = newans
                        N = set()
                    if newans == c:
                        N.add((nx, ny))
            if f:
                S.add((x, y))
        if N:
            l |= N
            l -= S
            for Nx, Ny in N:
                ans[Nx][Ny] = c
                if Nx == a and Ny == b:
                    return
        else:
            return


def intt(s):
    return int(s)+1


m, n, p = map(int, input().split())
l = ['#']
M = [l*(n+2)]+[l+input().split()+l for _ in range(m)]+[l*(n+2)]
for _ in range(p):
    x, y, a, b = map(intt, input().split())
    ans = [[-1]*(n+2) for i in range(m+2)]
    ans[x][y] = 0
    if M[x][y] == '#' or M[a][b] == '#':
        print('NO')
        continue
    bfs({(x, y)}, a, b)
    if ans[a][b] == -1:
        print('NO')
    else:
        print(ans[a][b])
