from sys import exit

m, n = map(int, input().split())
M = [[2]*(n+2)]
for i in range(m):
    M.append([2]+list(map(int, input().split()))+[2])
M.append([2]*(n+2))
if M[1][1] == 1:
    print(0)
    exit()
step, next = 0, 0
x = [1]
y = [1]
used = [[False]*(n+2) for i in range(m+2)]
used[1][1] = True
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while next != len(x):
    step += 1
    start = next
    next = len(x)
    for i in range(start, next):
        for j in range(4):
            newx = x[i]+dx[j]
            newy = y[i]+dy[j]
            if M[newy][newx] == 1:
                print(step)
                exit()
            elif not used[newy][newx] and M[newy][newx] == 0:
                x.append(newx)
                y.append(newy)
                used[newy][newx] = True
print('NO')
