from heapq import heappush, heappop
for _ in range(int(input())):
    n, m = map(int, input().split())
    M = [input() for _ in range(n)]
    f = [[1e6]*m for _ in range(n)]
    q = []
    for i in range(n):
        for j in range(m):
            if M[i][j] == 'r':
                heappush(q, (0, i, j))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ans = 'Impossible'
    while q:
        c, x, y = heappop(q)
        if M[x][y] == 'a':
            ans = c
            break
        for i in range(4):
            nx, ny, nc = x+dx[i], y+dy[i], c+1
            if 0 <= nx < n and 0 <= ny < m and M[nx][ny] != '#':
                if M[nx][ny] == 'x':
                    nc += 1
                if nc < f[nx][ny]:
                    f[nx][ny] = nc
                    heappush(q, (nc, nx, ny))
    print(ans)
