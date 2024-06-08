dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]
n = int(input())
x, y = map(int, input().split())
g = [set() for _ in range(n*n)]
for i in range(n*n):
    for k in range(8):
        if 0 <= i//n+dx[k] < n and 0 <= i % n + dy[k] < n:
            g[i].add(i+dx[k]*n+dy[k])

gone = [False]*(n*n)


def dfs(x, gone, k):
    if not k:
        print('success')
        exit()
    l = []
    for a in g[x]:
        if not gone[a]:
            c = 0
            for b in g[a]:
                if not gone[b]:
                    c += 1
            l.append((a, c))
    l.sort(key=lambda x: x[1])
    for a, _ in l:
        gone[a] = True
        dfs(a, gone, k-1)
        gone[a] = False


gone[x*n+y] = True
dfs(x*n+y, gone, n*n-1)
print('fail')
