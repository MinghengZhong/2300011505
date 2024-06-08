def H(n, a, b, c):
    if n:
        H(n-1, a, c, b)
        print('%d:%s->%s' % (n, a, c))
        H(n-1, b, a, c)


n, a, b, c = input().split()
H(int(n), a, b, c)
