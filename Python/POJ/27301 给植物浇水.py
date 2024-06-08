n, a, b = map(int, input().split())
l = list(map(int, input().split()))
aa, bb = a, b
ans = 0
for i in range((n+1)//2):
    if i == n-i-1:
        if max(aa, bb) < l[i]:
            ans += 1
        break
    if aa < l[i]:
        ans += 1
        aa = a
    if bb < l[n-i-1]:
        ans += 1
        bb = b
    aa -= l[i]
    bb -= l[n-i-1]
print(ans)
