def F(x):
    global p
    if p[x] != x:
        p[x] = F(p[x])
    return p[x]


def U(x, y):
    global p
    x = F(x)
    y = F(y)
    p[x] = y


n, k = map(int, input().split())
p = [i for i in range(3*n+1)]
ans = 0
for _ in range(k):
    d, x, y = map(int, input().split())
    if x > n or y > n:
        ans += 1
        continue
    if d == 1:
        if F(x+n) == F(y) or F(x+2*n) == F(y):
            ans += 1
            continue
        U(x, y)
        U(x+n, y+n)
        U(x+2*n, y+2*n)
    else:
        if F(x) == F(y) or F(x+2*n) == F(y):
            ans += 1
            continue
        U(x, y+2*n)
        U(x+n, y)
        U(x+2*n, y+n)
print(ans)
