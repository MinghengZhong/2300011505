from math import gcd
t = int(input())
ans = [0]*t
for _ in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    pos, zero, neg = 0, 0, 0
    for i in range(n):
        l[i] -= k
        if l[i] > 0:
            pos += 1
        elif l[i] < 0:
            neg += 1
        else:
            zero += 1
    if (pos and neg) or (pos and zero) or (neg and zero):
        ans[_] = -1
    elif pos:
        b = l[0]
        for i in range(1, n):
            b = gcd(l[i], b)
        for a in l:
            ans[_] += a//b-1
    elif neg:
        b = -l[0]
        for i in range(1, n):
            b = gcd(-l[i], b)
        for a in l:
            ans[_] += -a//b-1
for a in ans:
    print(a)
