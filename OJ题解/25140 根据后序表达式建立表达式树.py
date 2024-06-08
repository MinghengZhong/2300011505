from collections import defaultdict as D


for _ in range(int(input())):
    s = input()
    d = D(str)
    r = D(int)
    h = 0
    for i in range(len(s)-1, -1, -1):
        d[h] += s[i]
        r[h] -= 1
        if s[i] < 'a':
            h += 1
            r[h] += 2
        while not r[h]:
            h -= 1
    a = ''
    for i in range(max(d.keys()), -1, -1):
        a += d[i]
    print(a)
