a, b = input().split()
l = [a, b]+input().split()
if a == b:
    print(1)
    exit()
g = {s: set() for s in l}
for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        x, y = l[i], l[j]
        if sum(x[_] != y[_] for _ in range(len(a))) == 1:
            g[x].add(y)
            g[y].add(x)
f = {a}
q = [a]
s, e = 0, 1
c = 1
while s-e:
    c += 1
    for i in range(s, e):
        for p in g[q[i]]:
            if p == b:
                print(c)
                exit()
            if p not in f:
                q.append(p)
                f.add(p)
    s, e = e, len(q)
print(0)
