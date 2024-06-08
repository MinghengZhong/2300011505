n, m = map(int, input().split())
ans = 0
for _ in range(n):
    l = list(map(int, input().split()))
    b = []
    for i in range(m+1):
        b.append([0]*(m+2))
    for i in range(1, m+1):
        b[i][i] = l[i-1]*2
    for j in range(1, m):
        for i in range(1, m-j+1):
            b[i][i+j] = max(b[i+1][i+j]*2+l[i-1]*2, b[i][i+j-1]*2+l[i+j-1]*2)
    ans += b[1][m]
print(ans)
