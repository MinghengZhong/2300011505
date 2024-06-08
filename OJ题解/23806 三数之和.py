import bisect


def find(l, a):
    if l == []:
        return False
    return l[bisect.bisect(l, a)-1] == a


l = sorted(list(map(int, input().split())))
c1 = []
c2 = []
z = 0
for i in l:
    if i == 0:
        z += 1
    if c1 == []:
        c1 = [i]
    elif c1[-1] == i:
        c2.append(i)
    else:
        c1.append(i)
n = []
p = []
for a in c1:
    if a < 0:
        n.append(a)
    elif a > 0:
        p.append(a)
ans = 0
if z >= 3:
    ans += 1
if z >= 1:
    for a in p:
        if find(n, -a):
            ans += 1
for a in p:
    for b in n:
        if -b*2 <= a:
            break
        if find(n, -b-a):
            ans += 1
    if a % 2 == 0:
        if find(c2, -a//2):
            ans += 1
for a in n:
    for b in p:
        if -b*2 <= a:
            break
        if find(p, -b-a):
            ans += 1
    if a % 2 == 0:
        if find(c2, -a//2):
            ans += 1
print(ans)
