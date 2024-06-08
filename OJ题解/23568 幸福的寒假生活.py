def date(s):
    ans = int(s[2:])-7
    if s[0] == '2':
        ans += 31
    return ans


n = int(input())
l, ans = [], [0]*n
for _ in range(n):
    inp = input().split()
    l.append((date(inp[0]), date(inp[1]), int(inp[2])))
l.sort(key=lambda x: (x[1], x[0]))
for i in range(n):
    if l[i][1] > 44:
        break
    ans[i] = l[i][2]
    maxn = 0
    for j in range(i):
        if l[j][1] >= l[i][0]:
            break
        maxn = max(maxn, ans[j])
    ans[i] += maxn
print(max(ans))
