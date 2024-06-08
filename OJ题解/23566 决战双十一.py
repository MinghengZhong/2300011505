n, m = map(int, input().split())
ans = 0
count = [0]*m
for i in range(n):
    s, p = map(int, input().split())
    count[s-1] += p
    ans += p
ans -= (ans//200)*30
for i in range(m):
    q, x = map(int, input().split('-'))
    if count[i] >= q:
        ans -= x
print(ans)
