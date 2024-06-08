a, b, c = map(int, input().split())
l = [[0, 0]]
op = [0]
ans = 0
s, e = 0, 1
g = [[1]*(b+1) for _ in range(a+1)]
g[0][0] = 0
OP = ['FILL(1)', 'FILL(2)', 'DROP(1)', 'DROP(2)', 'POUR(1,2)', 'POUR(2,1)']


def F(x, y, z, i):
    global l, g, op
    if g[x][y]:
        l.append([x, y])
        g[x][y] = 0
        op.append(z+i)
        if x == c or y == c:
            print(ans)
            for s in str(op[-1]):
                print(OP[int(s)-1])
            exit()


while e-s:
    ans += 1
    for i in range(s, e):
        x, y = l[i]
        L = [[a, y], [x, b], [0, y], [x, 0]]
        if x+y <= b:
            L.append([0, x+y])
        else:
            L.append([x+y-b, b])
        if x+y <= a:
            L.append([x+y, 0])
        else:
            L.append([a, x+y-a])
        for j, X in enumerate(L):
            F(X[0], X[1], op[i]*10, j+1)
    s, e = e, len(l)
print('impossible')
