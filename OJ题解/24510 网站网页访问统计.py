from collections import defaultdict as D


def t(s):
    s = list(map(int, s.split(':')))
    return (s[0]*60+s[1])*60+s[2]


d = D(int)
m, M = 0, ''
for _ in range(int(input())):
    s = input().split()
    d[s[0]] += t(s[2])-t(s[1])
    if d[s[0]] > m:
        m = d[s[0]]
        M = s[0]
print(M)
