n = int(input())
l = []
for _ in range(n):
    l += [list(map(int, input().split()))]
ans = 0
for i in range(n//2):
    count = 0
    for j in range(i, n-i-1):
        count += l[i][j]+l[j][n-i-1]+l[n-i-1][n-j-1]+l[n-j-1][i]
    ans = max(ans, count)
if n % 2 == 1:
    ans = max(ans, l[n//2][n//2])
print(ans)
