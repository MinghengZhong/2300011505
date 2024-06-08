def dfs(used, x, y):
    global ans, l, xn, yn, dx, dy, xd, yd
    if (x == xn and y == yn) or (x+dx == xn and y+dy == yn):
        ans = True
    if ans:
        return
    for i in range(4):
        if l[x+xd[i]][y+yd[i]] != 1 and l[x+xd[i]+dx][y+yd[i]+dy] != 1 and not used[x+xd[i]][y+yd[i]]:
            used[x+xd[i]][y+yd[i]] = True
            dfs(used, x+xd[i], y+yd[i])
            used[x+xd[i]][y+yd[i]] = False
    return


ans = False
n = int(input())
l = [[1]*(n+2)]
for _ in range(n):
    l += [[1]+list(map(int, input().split()))+[1]]
l += [[1]*(n+2)]
x = []
y = []
xd = [-1, 0, 1, 0]
yd = [0, -1, 0, 1]
for i in range(1, n+1):
    for j in range(1, n+1):
        if l[i][j] == 5:
            x += [i]
            y += [j]
        if l[i][j] == 9:
            xn = i
            yn = j
dx, dy = 0, 0
if x[0] == x[1]:
    x0 = x[0]
    y0 = min(y)
    dy = 1
else:
    x0 = min(x)
    y0 = y[0]
    dx = 1
used = [[False]*(n+2) for i in range(n+2)]
used[x0][y0] = True
dfs(used, x0, y0)
if ans:
    print('yes')
else:
    print('no')
