from bisect import bisect

n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0
for i in range(n-1):
    new = l[2*i]+l[2*i+1]
    ans += new
    l.insert(bisect(l, new), new)
print(ans)
