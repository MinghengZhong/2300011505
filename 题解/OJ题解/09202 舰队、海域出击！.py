def dfs(x, d):
    global g, next, f
    for a in next[x]:
        if g[a]:
            g[a] = 0
            dfs(a, d | {a})
        else:
            if a in d:
                f = 1
        if f:
            return


def ans():
    global g, next, f
    f = 0
    n, m = map(int, input().split())
    g = [1]*n
    next = {i: set() for i in range(n)}
    for i in range(m):
        a, b = map(int, input().split())
        next[a-1].add(b-1)
    for i in range(n):
        if g[i]:
            g[i] = 0
            dfs(i, {i})
            if f:
                return 'Yes'
    return 'No'


for _ in range(int(input())):
    print(ans())
