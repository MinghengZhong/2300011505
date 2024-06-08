from collections import Counter
t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    l = Counter(input().split())
    count = 0
    for a in l.items():
        if a[0] != '1' and a[0] != '2':
            ans[_] += a[1]*(a[1]-1)//2
        else:
            count += a[1]
    ans[_] += count*(count-1)//2
for a in ans:
    print(a)
