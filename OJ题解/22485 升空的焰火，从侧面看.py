l, r = {}, {}
ans = []
for i in range(int(input())):
    l[i+1], r[i+1] = map(int, input().split())


def dfs(x, h):
    global ans
    if h == len(ans):
        ans.append(x)
    else:
        ans[h] = x
    if l[x]+1:
        dfs(l[x], h+1)
    if r[x]+1:
        dfs(r[x], h+1)


dfs(1, 0)
print(*ans)
