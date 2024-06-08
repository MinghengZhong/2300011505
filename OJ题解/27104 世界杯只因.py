n = int(input())
l = list(map(int, input().split()))
i = 0
ans = 0
while i < n:
    ans += 1
    next = -1
    for j in range(n):
        if abs(j-i) <= l[j]:
            next = max(next, j+l[j])
    i = next+1
print(ans)
