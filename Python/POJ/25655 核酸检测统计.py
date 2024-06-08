from collections import defaultdict as D


def j(l):
    l.sort()
    if l[0] != 1 or l[-1] < 7:
        return False
    for i in range(1, len(l)):
        if l[i]-l[i-1] > 3:
            return False
    return True


n = int(input())
m = int(input())
d = D(lambda: [])
e = D(str)
f = D(lambda: [0, 0])
A = 0
for _ in range(n):
    s = input().split()
    e[s[0]] = s[1]
    f[s[1]][0] += 1
for _ in range(m):
    s = input().split()
    d[s[1]].append(int(s[0]))
for a in d.items():
    if j(a[1]):
        f[e[a[0]]][1] += 1
    else:
        A += 1
print(A)
print(min(f.keys(), key=lambda x: f[x][1]/f[x][0]))
