n, m, a, b = map(int, input().split())
M = []
ans = 0


def walk(i, j):
    global M, ans, n, m
    if M[i][j]:
        return
    if i == n and j == m:
        ans += 1
        return
    if i+1 <= n:
        walk(i+1, j)
    if j+1 <= m:
        walk(i, j+1)
    return


def horse(i, j):
    global M, n, m
    if 0 <= i <= n and 0 <= j <= m:
        M[i][j] = True


for i in range(n+1):
    M.append([False]*(m+1))
M[a][b] = True
horse(a+1, b+2)
horse(a-1, b+2)
horse(a+1, b-2)
horse(a-1, b-2)
horse(a+2, b+1)
horse(a-2, b+1)
horse(a+2, b-1)
horse(a-2, b-1)
walk(0, 0)
print(ans)
