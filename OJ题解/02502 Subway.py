from heapq import heappush as I, heappop as O
from math import pow, sqrt


sx, sy, ex, ey = map(int, input().split())
X = [sx, ex]
Y = [sy, ey]
g = [[1]*203 for _ in range(203)]


def D(i, j):
    return sqrt(pow(X[i]-X[j], 2)+pow(Y[i]-Y[j], 2))


c = 1
while 1:
    try:
        l = list(map(int, input().split()))
    except EOFError:
        break
    for i in range(len(l)//2-1):
        c += 1
        X.append(l[2*i])
        Y.append(l[2*i+1])
        if i:
            g[c-1][c] = g[c][c-1] = 4
n = len(X)
f = [1]*n
m = [float('inf')]*n
m[0] = 0
q = [(0., 0)]
while q[0][1] != 1:
    c, i = O(q)
    f[i] = 0
    for j in range(n):
        if f[j]:
            s = c+D(i, j)/g[i][j]
            if s < m[j]:
                m[j] = s
                I(q, (s, j))
print(round(q[0][0]*(6e-3)))
