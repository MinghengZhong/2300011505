m, n = map(int, input().split())


def F(s):
    return 1-int(s)


M = [list(map(F, input().split())) for _ in range(m)]
for j in range(n):
    for i in range(1, m):
        M[i][j] = (M[i-1][j]+M[i][j])*M[i][j]
ans = 1
for i in range(m):
    for s in range(n-1):
        k = M[i][s]
        for e in range(s, n):
            if M[i][e] == 0:
                break
            k = min(k, M[i][e])
            ans = max(ans, k*(e-s+1))
print(ans)
