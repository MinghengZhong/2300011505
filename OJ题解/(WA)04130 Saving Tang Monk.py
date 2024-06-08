from heapq import heappop as O, heappush as I


def F(M):
    q = []
    t = [[[1e9]*(m+1) for i in range(n)] for j in range(n)]
    for X in range(n):
        for Y in range(n):
            if M[X][Y] == 'K':
                I(q, (0, 0, set(), X, Y))
                t[X][Y][0] = 0
                break
        if q:
            break
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        C, k, s, X, Y = O(q)
        if M[X][Y] == 'T' and k == m:
            return C
        for i in range(4):
            x, y, c = X+dx[i], Y+dy[i], C+1
            if 0 <= x < n and 0 <= y < n and M[x][y] != '#':
                if M[x][y] in '.T' and t[x][y][k] > c:
                    I(q, (c, k, s, x, y))
                    t[x][y][k] = c
                elif M[x][y] == 'S':
                    if (x, y) in s and t[x][y][k] > c:
                        I(q, (c, k, s, x, y))
                        t[x][y][k] = c
                    elif t[x][y][k] > c+1:
                        I(q, (c+1, k, s | {(x, y)}, x, y))
                        t[x][y][k] = c+1
                elif '0' < M[x][y] <= '9':
                    K = int(M[x][y])
                    if k > K-2 and t[x][y][max(k, K)] > c:
                        I(q, (c, max(k, K), s, x, y))
                        t[x][y][max(k, K)] = c
                    elif k < K-1 and t[x][y][k] > c:
                        I(q, (c, k, s, x, y))
                        t[x][y][k] = c
    return 'impossible'


while 1:
    n, m = map(int, input().split())
    if n == 0:
        break
    print(F([input() for _ in range(n)]))
