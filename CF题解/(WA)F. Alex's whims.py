for _ in range(int(input())):
    n, q = map(int, input().split())
    for i in range(n-1):
        print('%d %d' % (i+1, i+2))
    l, r = [i for i in range(1, n+1)], [1]
    for i in range(q):
        d = int(input())+1
        if len(l) == d or len(r) == d:
            print('-1 -1 -1')
        else:
            if len(l) > d:
                print('%d %d %d' % (l[d], l[d-1], r[-1]))
                r += l[d:]
                l = l[:d]
            else:
                d = len(l)+len(r)-d
                print('%d %d %d' % (r[d], r[d-1], l[-1]))
                l += r[d:]
                r = r[:d]
