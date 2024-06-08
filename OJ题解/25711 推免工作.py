def gpa(x):
    if x < 60:
        return 0
    else:
        return 4-3*(x-100)*(x-100)/1600


def GPA(l):
    n, m = 0, 0
    for i in range(0, len(l), 2):
        n += gpa(l[i])*l[i+1]
        m += l[i+1]
    return n/m


n, m = map(int, input().split())
d = {}
for _ in range(n):
    s = input().split()
    d[s[0]] = GPA(list(map(int, s[1:])))
print(' '.join(sorted(list(d.keys()), key=lambda a: -d[a])[:m]))
