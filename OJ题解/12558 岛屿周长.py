n, m = map(int, input().split())
M = [[0]*(m+2)]
for i in range(n):
    M += [[0]+list(map(int, input().split()))+[0]]
M += [[0]*(m+2)]
ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if M[i][j] != 0:
            ans += 4-(M[i+1][j]+M[i-1][j]+M[i][j+1]+M[i][j-1])
print(ans)
