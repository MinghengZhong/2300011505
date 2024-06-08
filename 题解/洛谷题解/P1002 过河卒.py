n, m, a, b = map(int, input().split())
M = []
ans = []


def horse(i, j):
    global M, n, m
    if 0 <= i <= n and 0 <= j <= m:
        M[i][j] = False


for i in range(n+1):
    M.append([True]*(m+1))
    ans.append([0]*(m+1))
M[a][b] = False
horse(a+1, b+2)
horse(a-1, b+2)
horse(a+1, b-2)
horse(a-1, b-2)
horse(a+2, b+1)
horse(a-2, b+1)
horse(a+2, b-1)
horse(a-2, b-1)
if M[0][0]:
    ans[0][0] = 1
for i in range(1, n+1):
    if M[i][0]:
        ans[i][0] = ans[i-1][0]
for j in range(1, m+1):
    if M[0][j]:
        ans[0][j] = ans[0][j-1]
for i in range(1, n+1):
    for j in range(1, m+1):
        if M[i][j]:
            ans[i][j] = ans[i-1][j]+ans[i][j-1]
print(ans[n][m])
