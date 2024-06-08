n = int(input())
l = []
for _ in range(n):
    l += [list(map(int, input().split()))]
l.sort(key=lambda a: [-a[1], a[0]])
count = 0
ans = 0
for a in l:
    count += a[0]
    ans = max(ans, count+a[1])
print(ans)
