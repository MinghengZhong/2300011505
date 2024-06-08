d, p = [], {}


def F(x):
    if p[x] != x:
        p[x] = F(p[x])
    return p[x]


for _ in range(int(input())-1):
    s = input().split()
    a = s[0]
    p[a] = a
    for i in range(int(s[1])):
        d.append((a, s[2+2*i], int(s[3+2*i])))
        p[s[2+2*i]] = s[2+2*i]
d.sort(key=lambda x: x[2])
ans = 0
for u, v, x in d:
    pu, pv = F(u), F(v)
    if pu != pv:
        p[pu] = pv
        ans += x
print(ans)
