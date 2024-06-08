n, m = map(int, input().split())
M = [[0]*n for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    M[y][x] = -1
    M[x][y] = -1
    M[x][x] += 1
    M[y][y] += 1
for i in range(n):
    for j in range(n):
        print(M[i][j], end='')
        if j != n-1:
            print(' ', end='')
    print('')
