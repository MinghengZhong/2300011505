n = int(input())
l = [int(input()) for _ in range(n)]
s, b = -1, -1
ans = 0
for i in range(n-1):
    s = b = l[i]
    for j in range(i+1, n):
        if l[j] <= s:
            break
        if l[j] > b:
            b = l[j]
            ans = max(ans, j-i+1)
print(ans)
