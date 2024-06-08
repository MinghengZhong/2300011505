import sys


def P(x):
    if p[x] != x:
        p[x] = P(p[x])
    return p[x]


sys.setrecursionlimit(1000000000)
for _ in range(int(input())):
    c = 'No s'
    n, m = map(int, input().split())
    p = [i for i in range(2*n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        if c != 'S':
            if P(a) == P(b) or P(a+n) == P(b+n):
                c = 'S'
            else:
                p[P(a)] = P(b+n)
                p[P(a+n)] = P(b)
    if _:
        print()
    print('Scenario #%d:' % (_+1))
    print(c+'uspicious bugs found!')
