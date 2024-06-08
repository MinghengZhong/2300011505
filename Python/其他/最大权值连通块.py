from collections import defaultdict as D
p = D(lambda: -1)


def F(x):
    global p
    if p[x]+1:
        px = F(p[x])
        p[x] = px
        return px
    return x


n, m = map(int, input().split())
l = list(map(int, input().split()))
for _ in range(m):
    x, y = map(int, input().split())
    px, py = F(x), F(y)
    if px != py:
        p[max(px, py)] = min(px, py)
ans = [0]*n
for i in range(n):
    ans[F(i)] += l[i]
print(max(ans))
