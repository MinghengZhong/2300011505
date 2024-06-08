def dfs(L, k):
    if not L or L == ['*']:
        return ''
    elif len(L) == 1:
        return L[0]
    s = L[0]
    q, n = [], len(L)
    for i in range(1, len(L)):
        if i != 1 and L[i][1] != '-':
            n = i
            break
        q.append(L[i][1:])
    l = dfs(q, k)
    q = []
    for i in range(n, len(L)):
        q.append(L[i][1:])
    r = dfs(q, k)
    if k == 0:
        return s+l+r
    elif k == 1:
        return l+r+s
    else:
        return l+s+r


n = int(input())
for _ in range(n):
    L = []
    while (s := input()) != '0':
        L.append(s)
    for i in range(3):
        print(dfs(L, i))
    if _ != n-1:
        print('')
