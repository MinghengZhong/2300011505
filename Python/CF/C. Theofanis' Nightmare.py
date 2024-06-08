t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    ans[_], count = sum(l), sum(l)
    for i in range(0, n-1):
        count -= l[i]
        if count > 0:
            ans[_] += count
for a in ans:
    print(a)
