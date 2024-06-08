from collections import defaultdict as D
n = int(input())
l = [input() for _ in range(n)]
b, g, p = D(set), D(set), {}
for s in l:
    b['_'+s[1:]].add(s)
    b[s[0]+'_'+s[2:]].add(s)
    b[s[:2]+'_'+s[3]].add(s)
    b[s[:3]+'_'].add(s)
for a in b.values():
    for x in a:
        for y in a:
            if x != y:
                g[x].add(y)
a, b = input().split()
if a == b:
    print(a)
    exit()
l = [a]
gone = set([a])
s, e = 0, 1
while s != e:
    for i in range(s, e):
        for a in g[l[i]]:
            if a not in gone:
                p[a] = l[i]
                gone.add(a)
                l.append(a)
            if a == b:
                ans = [b]
                while True:
                    b = p[b]
                    ans.append(b)
                    if b == l[0]:
                        break
                print(*ans[::-1])
                exit()
    s, e = e, len(l)
print('NO')
