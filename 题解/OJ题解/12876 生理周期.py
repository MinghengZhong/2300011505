def g(a, b, c):
    l = [0]*a
    for i in range(a):
        l[(i*b*c) % a] = i
    return l


a, b, c, n = g(23, 28, 33), g(28, 33, 23), g(33, 23, 28), 0
while True:
    p, e, i, d = map(int, input().split())
    if p == -1:
        break
    n += 1
    ans = (28*33*a[p % 23]+33*23*b[e % 28]+23*28*c[i % 33]-d) % 21252
    if ans <= 0:
        ans += 21252
    print('Case %d: the next triple peak occurs in %d days.' % (n, ans))
