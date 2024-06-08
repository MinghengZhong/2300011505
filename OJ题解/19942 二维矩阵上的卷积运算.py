m, n, p, q = map(int, input().split())
M = []
K = []
for i in range(m):
    M.append(list(map(int, input().split())))
for i in range(p):
    K.append(list(map(int, input().split())))
for i in range(m-p+1):
    for j in range(n-q+1):
        ans = 0
        for y in range(p):
            for x in range(q):
                ans += M[i+y][j+x]*K[y][x]
        print(ans, end='')
        if j != n-q+1:
            print(' ', end='')
    print('')
