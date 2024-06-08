sss = input().split()
n = int(sss[0])
l = int(sss[1])
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(0, n-1):
    if a[i+1]-a[i] > ans:
        ans = a[i+1]-a[i]
ans /= 2
if a[0] > ans:
    ans = a[0]
if l-a[-1] > ans:
    ans = l-a[-1]
print(ans)
