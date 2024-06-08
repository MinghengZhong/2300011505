from heapq import heappush as I, heappop as O

while 1:
    if (n := int(input())) == 0:
        break
    g = [[0]*n for _ in range(n)]
    m = [1e9]*n
    f = [1]*n
    l = []
    for i in range(n):
        a = input()
        for j in range(i):
            g[i][j] = g[j][i] = sum(a[_] != l[j][_] for _ in range(len(a)))
        l.append(a)
    q = [(0, 0)]
    a = b = 0
    while b-n:
        c, x = O(q)
        if f[x]:
            b += 1
            a += c
            f[x] = 0
            for i in range(n):
                if f[i] and g[i][x] < m[i]:
                    I(q, (g[i][x], i))
                    m[i] = g[i][x]
    print('The highest possible quality is 1/%d.' % a)
