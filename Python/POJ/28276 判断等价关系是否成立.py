def P(x):
    if p[x] != x:
        p[x] = P(p[x])
    return p[x]


n = int(input())
p = {}
g = set()
l = []
ans = 'True'
for _ in range(n):
    s = input()
    a, b = s[0], s[3]
    if a not in g:
        g.add(a)
        p[a] = a
    if b not in g:
        g.add(b)
        p[b] = b
    if s[1] == '=':
        p[P(a)] = P(b)
    else:
        l.append((a, b))
for a, b in l:
    if P(a) == P(b):
        ans = 'False'
print(ans)
