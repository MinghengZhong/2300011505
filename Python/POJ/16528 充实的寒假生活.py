n = int(input())
l = []
for i in range(n):
    l.append(tuple(map(int, input().split())))
l.sort(key=lambda x: (x[1], x[0]))
ans = 0
i, last = 0, -1
while True:
    while l[i][0] <= last or l[i][1] > 60:
        i += 1
        if i == n:
            break
    if i == n:
        break
    last = l[i][1]
    ans += 1
print(ans)
