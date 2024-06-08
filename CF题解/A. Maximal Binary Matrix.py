n, k = map(int, input().split())
if k > n*n:
    print(-1)
else:
    M = [['0']*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if M[i][j] == '0':
                if k > 1:
                    if i == j:
                        k -= 1
                        M[i][j] = '1'
                    else:
                        k -= 2
                        M[i][j] = '1'
                        M[j][i] = '1'
                elif k == 1:
                    if i == j:
                        k -= 1
                        M[i][j] = '1'
                        break
                else:
                    break
        if k == 0:
            break
    for i in range(n):
        print(' '.join(M[i]))
