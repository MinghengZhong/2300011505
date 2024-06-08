for i in range(int(input())):
    a, b = map(int, input().split())
    l = r = 0
    while a-1 and b-1:
        if a > b:
            l += a//b
            a = a % b
        else:
            r += b//a
            b = b % a
    l += a-1
    r += b-1
    print('Scenario #%d:\n%d %d\n' % (i+1, l, r))
