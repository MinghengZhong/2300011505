n = int(input())
M = [[0]*(n+2)]
for i in range(n):
    M += [[0]+[-1]*n+[0]]
M += [[0]*(n+2)]
lx = [1, 0, -1, 0]
ly = [0, 1, 0, -1]
j = 0
x = 0
y = 1
for i in range(1, n**2+1):
    if M[y+ly[j]][x+lx[j]] != -1:
        j = (j+1) % 4
    x += lx[j]
    y += ly[j]
    M[y][x] = i
for i in range(1, n+1):
    print(' '.join(map(str, M[i][1:-1])))
