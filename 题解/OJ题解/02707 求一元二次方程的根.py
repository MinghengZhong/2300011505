n = int(input())
for i in range(n):
    a, b, c = map(float, input().split())
    delta = b*b-4*a*c
    zero = -b/(2*a)
    if a < 0:
        a = -a
    if zero == 0:
        zero = 0
    if delta == 0:
        print('x1=x2=%.5f' % (zero))
    elif delta < 0:
        print('x1=%.5f+%.5fi' % (zero, ((-delta)**.5)/(2*a)), end=';')
        print('x2=%.5f-%.5fi' % (zero, ((-delta)**.5)/(2*a)))
    else:
        print('x1=%.5f' % (zero+(delta**.5)/(2*a)), end=';')
        print('x2=%.5f' % (zero-(delta**.5)/(2*a)))
