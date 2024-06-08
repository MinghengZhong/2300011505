from math import gcd
t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    l = sorted(list(map(int, input().split())))
    if n == 1:
        ans[_] = 1
        continue
    k = l[1]-l[0]
    for i in range(2, n):
        k = gcd(l[i]-l[i-1], k)
    for a in l:
        ans[_] += (l[-1]-a)//k
    a = n
    for i in range(n-2, -1, -1):
        if (l[-1]-l[i+1])//k+1 >= a:
            break
        elif l[i+1]-l[i] > k:
            a = (l[-1]-l[i+1])//k+1
            break
    ans[_] += a
for a in ans:
    print(a)
