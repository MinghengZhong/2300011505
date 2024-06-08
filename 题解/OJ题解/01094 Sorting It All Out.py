def dfs(a):
    global g, f
    f[a] = 0
    S = list(g[a])
    for s in S:
        g[a] |= g[s]
        if f[s]:
            dfs(s)
    return


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    ans = 'Sorted sequence cannot be determined.'
    g = [set() for _ in range(n)]
    q = []
    for _ in range(m):
        s = input()
        q.append((ord(s[0])-65, ord(s[2])-65))
    for i in range(m):
        a, b = q[i]
        g[b] |= {a}
        f = [1]*n
        for j in range(n):
            if f[j]:
                dfs(j)
        for j in range(n):
            if j in g[j]:
                ans = 'Inconsistency found after %d relations.' % (i+1)
                break
        if i >= n-2 and ans[-2] == 'd':
            l = sorted(g, key=lambda x: len(x))+[{_ for _ in range(n)}]
            o = ''
            for j in range(n+1):
                if len(l[j]) != j:
                    break
                if j:
                    for c in l[j]-l[j-1]:
                        o += chr(c+65)
                if j == n:
                    ans = 'Sorted sequence determined after %d relations: %s.' % (
                        i+1, o)
        if ans[-2] != 'd':
            break
    print(ans)
