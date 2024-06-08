n, m = map(int, input().split())
l = list(map(int, input().split()))
ans = 1
count = 0
for a in l:
    if count+a <= m:
        count += a
    else:
        count = a
        ans += 1
print(ans)
