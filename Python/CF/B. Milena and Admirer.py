from math import ceil
t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    last = l[-1]
    for i in range(n-1, -1, -1):
        ans[_] += ceil(l[i]/last)-1
        last = l[i]//ceil(l[i]/last)
for a in ans:
    print(a)
