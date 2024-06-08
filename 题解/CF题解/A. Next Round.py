l = list(map(int, input().split()))
a = list(map(int, input().split()))
n = l[0]
k = l[1]
ans = 0
for i in range(0, n):
    if a[i] >= a[k-1] and a[i] > 0:
        ans += 1
print(ans)
