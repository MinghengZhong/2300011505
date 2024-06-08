from heapq import heappush, heappop
from collections import defaultdict
q = int(input())
l, r, ans = [], [], [False]*q
ll, rr = defaultdict(int), defaultdict(int)
for i in range(q):
    s, a, b = input().split()
    a, b = int(a), int(b)
    if s == '+':
        ll[a] += 1
        rr[b] += 1
        heappush(l, -a)
        heappush(r, b)
    else:
        ll[a] -= 1
        rr[b] -= 1
    while l and ll[-l[0]] == 0:
        heappop(l)
    while r and rr[r[0]] == 0:
        heappop(r)
    if l and r and -l[0] > r[0]:
        ans[i] = True
for a in ans:
    if a:
        print('YES')
    else:
        print('NO')
