n, m = map(int, input().split())
l = list(map(int, input().split()))
now = 1
ans = 0
for a in l:
    if a > now:
        ans += a-now
        now = a
    elif a < now:
        ans += n+a-now
        now = a
print(ans)
