def bfs(l, n, m):
    used = [[False]*(m+2) for _ in range(n+2)]
    x = [1]
    y = [1]
    li = [1, 0, -1, 0]
    lj = [0, 1, 0, -1]
    head = 0
    tail = 1
    while head < tail:
        for i in range(head, tail):
            for j in range(4):
                if l[x[i]+li[j]][y[i]+lj[j]] == '.' and not used[x[i]+li[j]][y[i]+lj[j]]:
                    if x[i]+li[j] == n and y[i]+lj[j] == m:
                        return 'Yes'
                    used[x[i]+li[j]][y[i]+lj[j]] = True
                    x += [x[i]+li[j]]
                    y += [y[i]+lj[j]]
        head = tail
        tail = len(x)
    return 'No'


n, m = map(int, input().split())
l = ['#'*(m+2)]
for _ in range(n):
    l += ['#'+input()+'#']
l += ['#'*(m+2)]
print(bfs(l, n, m))
