m, n, t = map(int, input().split())
M = [input() for _ in range(m)]
x = y = f = 0
for i in range(m):
    for j in range(n):
        if M[i][j] == '@':
            x, y = i, j
            f = 1
            break
    if f:
        break
s, e = 0, 1
l = [(x, y, t)]
g = [[-1]*n for i in range(m)]
g[x][y] = t
c = 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
while s != e:
    c += 1
    for i in range(s, e):
        for j in range(4):
            x, y, k = l[i][0]+dx[j], l[i][1]+dy[j], l[i][2]
            if x in (-1, m) or y in (-1, n):
                continue
            if M[x][y] == '+':
                print(c)
                exit()
            elif M[x][y] == '#':
                if k-1 > g[x][y]:
                    g[x][y] = k-1
                    l.append((x, y, k-1))
            elif M[x][y] == '*':
                if k > g[x][y]:
                    g[x][y] = k
                    l.append((x, y, k))
    s, e = e, len(l)
print(-1)
