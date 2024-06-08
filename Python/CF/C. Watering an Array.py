t = int(input())
ans = [0]*t


def count(l):
    re = 0
    for i in range(len(l)):
        if l[i] == i+1:
            re += 1
    return re


for _ in range(t):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(min(2*(n+1), d)):
        ans[_] = max(ans[_], count(a)+(d-i-1)//2)
        for j in range(b[i % k]):
            a[j] += 1
for a in ans:
    print(a)
