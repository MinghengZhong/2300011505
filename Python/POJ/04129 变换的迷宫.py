def bfs(M):
    g = [[set() for i in range(C)] for j in range(R)]
    l = []
    for X in range(R):
        for Y in range(C):
            if M[X][Y] == 'S':
                l.append((X, Y))
                g[X][Y].add(0)
                break
        if l:
            break
    s, e, c = 0, 1, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while s-e:
        c += 1
        for i in range(s, e):
            x, y = l[i]
            for j in range(4):
                nx, ny = x+dx[j], y+dy[j]
                if 0 <= nx < R and 0 <= ny < C and c % K not in g[nx][ny]:
                    if M[nx][ny] == 'E':
                        return c
                    if M[nx][ny] != '#' or c % K == 0:
                        g[nx][ny].add(c % K)
                        l.append((nx, ny))
        s, e = e, len(l)
    return 'Oop!'


for _ in range(int(input())):
    R, C, K = map(int, input().split())
    print(bfs([input() for i in range(R)]))
