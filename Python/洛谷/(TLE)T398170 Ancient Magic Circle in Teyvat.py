n, m = map(int, input().split())
red = [[False]*n for i in range(n)]
R = []
B = []

for i in range(m):
    i, j = map(int, input().split())
    red[i-1][j-1] = True
for i in range(n):
    R.append([])
    B.append([])
    for j in range(i+1, n):
        if red[i][j]:
            R[i].append(j)
        else:
            B[i].append(j)
r = 0
b = 0
for i1 in range(n-3):
    for i2 in R[i1]:
        for i3 in R[i2]:
            if red[i1][i3]:
                for i4 in R[i3]:
                    if red[i1][i4] and red[i2][i4]:
                        r += 1
for i1 in range(n-3):
    for i2 in B[i1]:
        for i3 in B[i2]:
            if not red[i1][i3]:
                for i4 in B[i3]:
                    if not red[i1][i4] and not red[i2][i4]:
                        b += 1
print(abs(r-b))
