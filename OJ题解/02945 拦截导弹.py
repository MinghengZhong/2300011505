n = int(input())
l = list(map(int, input().split()))
ans = [1]*n
for i in range(n):
    for j in range(i):
        if l[j] >= l[i]:
            ans[i] = max(ans[i], ans[j]+1)
print(max(ans))
