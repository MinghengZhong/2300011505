from math import pow
n = int(input())
M = [list(map(int, input().split())) for _ in range(8)]
L = {}
s = sum(sum(l) for l in M)/n
ans = 1e9
for a in range(8):
    for c in range(a, 8):
        for b in range(8):
            for d in range(b, 8):
                L[(a, b, c, d)] = pow(sum(sum(M[i][j] for j in range(b, d+1))
                                          for i in range(a, c+1))-s, 2)


def cut(a, b, c, d, x, y):
    global ans
    if x > ans:
        return
    if y:
        for i in range(a, c):
            cut(i+1, b, c, d, x+L[(a, b, i, d)], y-1)
            cut(a, b, i, d, x+L[(i+1, b, c, d)], y-1)
        for i in range(b, d):
            cut(a, i+1, c, d, x+L[(a, b, c, i)], y-1)
            cut(a, b, c, i, x+L[(a, i+1, c, d)], y-1)
    else:
        ans = min(ans, x+L[(a, b, c, d)])


cut(0, 0, 7, 7, 0, n-1)
print('%.3f' % pow(ans/n, 1/2))
