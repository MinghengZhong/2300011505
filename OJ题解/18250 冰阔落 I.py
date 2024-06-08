from collections import defaultdict as D
p = D(int)


def F(x):
    global p
    if p[x]:
        px = F(p[x])
        p[x] = px
        return px
    return x


while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break
    p = D(int)
    a = n
    for _ in range(m):
        x, y = map(int, input().split())
        px, py = F(x), F(y)
        if px-py:
            p[py] = px
            print('No')
        else:
            print('Yes')
    s = sorted(list(set([F(i) for i in range(1, n+1)])))
    print(len(s))
    print(' '.join(map(str, s)))
