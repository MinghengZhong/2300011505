t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    ans[_] = n-sum(l)
    i = 0
    while l[i] == 0:
        i += 1
        ans[_] -= 1
    i = n-1
    while l[i] == 0:
        i -= 1
        ans[_] -= 1
for a in ans:
    print(a)
