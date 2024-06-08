t = int(input())
ans = [0]*t
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    ans[i] += l[0]-1
    for j in range(1, n):
        ans[i] += max(l[j]-l[j-1], 0)
for a in ans:
    print(a)
