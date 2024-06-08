t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    l, used, count = [], [False]*n, 0
    for i in range(n):
        l.append((s[2*i], s[2*i+1]))
    l.sort(key=lambda x: (x[0], x[1]))
    while count < n:
        l1, l2 = 0, 0
        ans[_] += 1
        for i in range(n):
            if not used[i] and l1 <= l[i][0] and l2 <= l[i][1]:
                count += 1
                used[i] = True
                l1, l2 = l[i][0], l[i][1]
for a in ans:
    print(a)
