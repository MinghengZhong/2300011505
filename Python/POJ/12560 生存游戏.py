n, m = map(int, input().split())
M = [[0]*(m+2)]
for i in range(n):
    s = list(map(int, input().split()))
    M.append([0]+s+[0])
M.append([0]*(m+2))
for i in range(1, n+1):
    for j in range(1, m+1):
        count = M[i+1][j]+M[i][j+1]+M[i-1][j]+M[i][j-1] + \
            M[i+1][j+1]+M[i-1][j+1]+M[i-1][j-1]+M[i+1][j-1]
        if count == 3:
            print(1, end='')
        elif count == 2:
            print(M[i][j], end='')
        else:
            print(0, end='')
        if j != m:
            print(' ', end='')
    print('')
