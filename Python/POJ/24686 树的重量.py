from math import log2
k, n = map(int, input().split())
a, b = [0]*(1 << k), [0]*(1 << k)
for _ in range(n):
    s = input().split()
    x = int(s[1])
    l = (1 << (k-int(log2(x))))-1
    if s[0] == '1':
        y = int(s[2])
        a[x] += y
        while x:
            b[x] += y*l
            x >>= 1
    else:
        ans = b[x]
        while x:
            x >>= 1
            ans += a[x]*l
        print(ans)
