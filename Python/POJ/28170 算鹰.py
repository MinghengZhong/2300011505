M = [input() for _ in range(10)]
g = [[1]*10 for _ in range(10)]
ans = 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def dfs(i, j):
    global g
    g[i][j] = 0
    for k in range(4):
        x, y = i+dx[k], j+dy[k]
        if 0 <= x < 10 and 0 <= y < 10 and g[x][y] and M[x][y] == '.':
            dfs(x, y)


for i in range(10):
    for j in range(10):
        if g[i][j] and M[i][j] == '.':
            ans += 1
            dfs(i, j)
print(ans)
