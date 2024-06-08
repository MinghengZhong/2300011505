dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]


def dfs(n, m, x, y, gone):
    if len(gone) == n*m:
        return 1
    a = 0
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        idx = nx+ny*n
        if 0 <= nx < n and 0 <= ny < m and idx not in gone:
            gone.add(idx)
            a += dfs(n, m, nx, ny, gone)
            gone.remove(idx)
    return a


for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    print(dfs(n, m, x, y, set([x+y*n])))
