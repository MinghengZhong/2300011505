n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
d = []
for i in range(n-1):
    d.append(l[i+1]-l[i])
d.sort(reverse=True)
ans = l[-1]-l[0]
for a in d:
    m -= 1
    ans -= a
    if m == 1:
        break
print(ans)
