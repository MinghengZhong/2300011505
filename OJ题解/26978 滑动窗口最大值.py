from collections import deque
ans = []
d = deque()
n, k = map(int, input().split())
l = list(map(int, input().split()))
for i in range(n):
    if i >= k and d[0] == l[i-k]:
        d.popleft()
    while d and d[-1] < l[i]:
        d.pop()
    d.append(l[i])
    if i >= k-1:
        ans.append(d[0])
print(' '.join(map(str, ans)))
