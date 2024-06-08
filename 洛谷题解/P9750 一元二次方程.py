import math


def ans1(p, q):
    if p == 0:
        return '0'
    g = math.gcd(p, q)
    if g == abs(q):
        return str(p//q)
    else:
        if q > 0:
            return '%d/%d' % (p // g, q // g)
        else:
            return '%d/%d' % (-p//g, -q//g)


def ans2(d, q):
    p = 1
    for i in range(int(d**.5), 1, -1):
        if d % (i**2) == 0:
            p = i
            break
    d = d//(p**2)
    g = math.gcd(p, q)
    if g == q:
        if p == q:
            return 'sqrt(%d)' % (d)
        else:
            return '%d*sqrt(%d)' % (p//g, d)
    elif g == p:
        if p == q:
            return 'sqrt(%d)' % (d)
        else:
            return 'sqrt(%d)/%d' % (d, q//g)
    else:
        return '%d*sqrt(%d)/%d' % (p//g, d, q//g)


n, N = map(int, input().split())
for _ in range(n):
    a, b, c = map(int, input().split())
    d = b**2-4*a*c
    if d < 0:
        ans = 'NO'
    else:
        if int(d**.5) == d**.5:
            if a > 0:
                ans = ans1(-b+int(d**.5), 2*a)
            else:
                ans = ans1(-b-int(d**.5), 2*a)
        else:
            if b == 0:
                if a > 0:
                    ans = ans2(d, 2*a)
                else:
                    ans = ans2(d, -2*a)
            else:
                if a > 0:
                    ans = ans1(-b, 2*a)+'+'+ans2(d, 2*a)
                else:
                    ans = ans1(-b, 2*a)+'+'+ans2(d, -2*a)
    print(ans)
