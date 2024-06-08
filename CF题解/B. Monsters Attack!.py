from collections import defaultdict
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    d = defaultdict(int)
    for i in range(n):
        d[abs(l[i])] += a[i]
    d = sorted(list(d.items()), key=lambda x: x[0])
    ans, count = True, 0
    for a in d:
        count += a[1]
        if count > a[0]*k:
            ans = False
            break
    if ans:
        print('YES')
    else:
        print('NO')
