def F(s, n):
    c = 1
    for i in range(n):
        c -= 2*(s[i] == '#')-1
        if c == 0 and i != n-1:
            return 0
    return c == 0


while 1:
    n = int(input())
    if n == 0:
        break
    print('FT'[F(input().split(), n)])
