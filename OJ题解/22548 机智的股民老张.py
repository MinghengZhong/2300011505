l, ans = list(map(int, input().split())), 0
for i in range(1, len(l)):
    ans = max(ans, l[i]-l[i-1])
    l[i] = min(l[i], l[i-1])
print(ans)
