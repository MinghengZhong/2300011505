from collections import defaultdict as D
import heapq as H
l = []
d = D(str)
n = int(input())
for _ in range(n):
    s = input().split()
    l.append((int(s[1]), list(s[0])))
H.heapify(l)
for _ in range(n-1):
    a = H.heappop(l)
    b = H.heappop(l)
    a, b = max(a, b), min(a, b)
    for c in a[1]:
        d[c] = '1'+d[c]
    for c in b[1]:
        d[c] = '0'+d[c]
    H.heappush(l, (a[0]+b[0], sorted(a[1]+b[1])))
e = {a[1]: a[0] for a in d.items()}
while True:
    try:
        s = input()
    except EOFError:
        break
    if s[0] in '01':
        A = B = ''
        for a in s:
            A += a
            try:
                B += e[A]
                A = ''
            except KeyError:
                continue
        print(B)
    else:
        print(''.join(d[a] for a in s))
