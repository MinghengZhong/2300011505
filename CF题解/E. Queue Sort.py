t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    ans[_] = l.index(min(l))
    for i in range(ans[_]+1, n):
        if l[i] < l[i-1]:
            ans[_] = -1
            break
for a in ans:
    print(a)
