from collections import defaultdict as D
left, right = {}, {}
ans = D(lambda: [])


def build(n, node):
    if n < node:
        try:
            build(n, left[node])
        except KeyError:
            left[node] = n
    elif n > node:
        try:
            build(n, right[node])
        except KeyError:
            right[node] = n


def dfs(node, h):
    global ans
    ans[h].append(node)
    try:
        dfs(left[node], h+1)
    except KeyError:
        pass
    try:
        dfs(right[node], h+1)
    except KeyError:
        pass


l = list(map(int, input().split()))
for i in range(1, len(l)):
    build(l[i], l[0])
dfs(l[0], 0)
ans[0] = [l[0]]
a = []
for i in range(max(ans.keys())+1):
    a += ans[i]
print(' '.join(map(str, a)), end='')
