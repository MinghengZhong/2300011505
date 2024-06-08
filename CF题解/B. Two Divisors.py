from math import gcd
t = int(input())
ans = [0]*t
for _ in range(t):
    a, b = map(int, input().split())
    c = gcd(a, b)
    if a == c:
        ans[_] = (b**2)//a
    else:
        ans[_] = a*b//c
for a in ans:
    print(a)
