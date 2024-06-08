t = int(input())
anss = [0]*t
for _ in range(t):
    n = int(input())
    s = '0'+input()
    l, r = [0]*(n+1), [0]*(n+1)
    for i in range(1, n+1):
        l[i], r[i] = map(int, input().split())
    ans, q = n, [(1, 0)]
    while q:
        i, count = q.pop()
        if l[i] == r[i] == 0:
            ans = min(ans, count)
            continue
        if l[i]:
            q.append((l[i], count+(s[i] != 'L')))
        if r[i]:
            q.append((r[i], count+(s[i] != 'R')))
    anss[_] = ans
for ans in anss:
    print(ans)
