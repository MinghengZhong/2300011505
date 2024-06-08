n, m = map(int, input().split())
gone = [[False]*(m+2) for _ in range(n+2)]
map = ['.'*(m+2)]+['.'+input()+'.' for _ in range(n)]+['.'*(m+2)]
dx, dy = [1, 1, 1, 0, 0, -1, -1, -1], [0, 1, -1, 1, -1, 0, 1, -1]
ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if map[i][j] == '.' or gone[i][j]:
            continue
        ans += 1
        lx, ly = [i], [j]
        gone[i][j] = True
        s, e = 0, 1
        while s != e:
            for a in range(s, e):
                for b in range(8):
                    x, y = lx[a]+dx[b], ly[a]+dy[b]
                    if map[x][y] == '.' or gone[x][y]:
                        continue
                    lx.append(x)
                    ly.append(y)
                    gone[x][y] = True
            s, e = e, len(lx)
print(ans)
