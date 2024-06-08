n = int(input())
l = list(map(int, input().split()))
l.sort()
time = 0
ans = 0
for i in range(n):
    if time <= l[i]:
        ans += 1
        time += l[i]
print(ans)
