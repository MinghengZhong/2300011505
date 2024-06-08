n, n1, n2 = map(int, input().split())
ans = []
for i in range(n):
    ans.append([0]*n)
m1x = []
m1y = []
m1 = []
m2x = []
m2y = []
m2 = []
for i in range(n1):
    x, y, num = map(int, input().split())
    m1x.append(x)
    m1y.append(y)
    m1.append(num)
for i in range(n2):
    x, y, num = map(int, input().split())
    m2x.append(x)
    m2y.append(y)
    m2.append(num)
for i in range(n1):
    for j in range(n2):
        if m1y[i] == m2x[j]:
            ans[m1x[i]][m2y[j]] += m1[i]*m2[j]
for i in range(n):
    for j in range(n):
        if ans[i][j] != 0:
            print('%d %d %d' % (i, j, ans[i][j]))
