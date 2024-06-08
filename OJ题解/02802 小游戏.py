t, n, m, ans = 0, 0, 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
used = []
M = []


def check(x, y, a, b):
    global used
    if x == a and y == b:
        return True
    return M[y+1][x+1] == ' ' and not used[y][x]


def bfs(x, y, a, b):
    global used, ans
    used = [[False]*(n+2) for i in range(m+2)]
    lx = [x]
    ly = [y]
    start = 0
    used[y][x] = True
    seg = 0
    while start != len(lx):
        seg += 1
        end = len(lx)
        for i in range(start, end):
            for k in range(4):
                newx = lx[i]+dx[k]
                newy = ly[i]+dy[k]
                while check(newx, newy, a, b):
                    if newx == a and newy == b:
                        ans = seg
                        return
                    lx.append(newx)
                    ly.append(newy)
                    used[newy][newx] = True
                    newx = newx+dx[k]
                    newy = newy+dy[k]
        start = end
    return


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    t += 1
    M = ['X'*(n+4), 'X'+' '*(n+2)+'X']
    for _ in range(m):
        M.append('X '+input()+' X')
    M += ['X'+' '*(n+2)+'X', 'X'*(n+4)]
    print('Board #%d:' % t)
    tt = 0
    while True:
        x, y, a, b = map(int, input().split())
        if x == y == a == b == 0:
            break
        tt += 1
        ans = -1
        bfs(x, y, a, b)
        if ans == -1:
            print('Pair %d: impossible.' % tt)
        else:
            print('Pair %d: %d segments.' % (tt, ans))
    print('')
