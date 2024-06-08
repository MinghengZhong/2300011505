ans, l, r = 1, [-1], [-1]


def dfs(n, count):
    global ans, l, r
    if l[n] != -1:
        dfs(l[n], count+1)
    if r[n] != -1:
        dfs(r[n], count+1)
    ans = max(ans, count)


n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    l.append(a)
    r.append(b)
dfs(1, 1)
print(ans)
