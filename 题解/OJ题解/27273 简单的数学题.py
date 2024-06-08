from math import log2
t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    a = n*(n+1)//2
    b = int(log2(n))
    a -= 2*((2 << b)-1)
    ans[_] = a
for a in ans:
    print(a)
