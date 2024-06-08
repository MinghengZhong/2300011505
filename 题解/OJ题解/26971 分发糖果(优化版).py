n = int(input())
l = list(map(int, input().split()))
ans = 0
up = [1]*n
down = [1]*n
for i in range(n-1):
    if l[i+1] > l[i]:
        up[i+1] = up[i]+1
    if l[n-i-2] > l[n-i-1]:
        down[n-i-2] = down[n-i-1]+1
for i in range(n):
    ans += max(up[i], down[i])
print(ans)
