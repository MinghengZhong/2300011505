m, n = map(int, input().split())
M = [[0]*(n+1)]
for _ in range(m):
    M.append([0]+list(map(int, input().split())))
if m == 1 and n == 1:
    print(0)
else:
    l = [[[0]*(m+1) for i in range(m+1)] for j in range(m+n-2)]
    l[1][1][2] = M[1][2]+M[2][1]
    for step in range(2, m+n-2):
        for i in range(max(1, step-n+2), min(m, step+1)):
            for j in range(i+1, min(m+1, step+2)):
                if j-i == 1:
                    l[step][i][j] = M[i][step-i+2]+M[i+1][step-i+1] +\
                        max(l[step-1][i-1][i], l[step-1]
                            [i-1][i+1], l[step-1][i][i+1])
                else:
                    l[step][i][j] = M[i][step-i+2]+M[j][step-j+2] + \
                        max(l[step-1][i-1][j-1], l[step-1][i-1][j],
                            l[step-1][i][j-1], l[step-1][i][j])
    print(l[m+n-3][m-1][m])
