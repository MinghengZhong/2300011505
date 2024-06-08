from collections import defaultdict as D
n = int(input())
d = D(str)
h = 0
ans = ''
for s in input().split():
    if s[0] != '$':
        d[h] = s[0]+d[h]
    h -= 2*(int(s[1]))-1
for a in d.values():
    ans += a
print(' '.join(ans))
