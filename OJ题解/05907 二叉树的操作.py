for _ in range(int(input())):
    n, m = map(int, input().split())
    l, r, p = {}, {}, {}
    for i in range(n):
        x, L, R = map(int, input().split())
        l[x], r[x], p[L], p[R] = L, R, x, x
    for i in range(m):
        s = input().split()
        x = int(s[1])
        if s[0] == '1':
            y = int(s[2])
            P = p[x]
            if p[x]-p[y]:
                if l[P] == x:
                    l[P] = y
                else:
                    r[P] = y
                P = p[y]
                if l[P] == y:
                    l[P] = x
                else:
                    r[P] = x
                p[x], p[y] = p[y], p[x]
            else:
                l[P], r[P] = r[P], l[P]
        else:
            while l[x]+1:
                x = l[x]
            print(x)
