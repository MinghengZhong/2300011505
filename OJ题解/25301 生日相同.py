from collections import defaultdict
d = defaultdict(lambda: [])
for _ in range(int(input())):
    s = input().split()
    d[(int(s[1]), int(s[2]))].append(s[0])
for a in sorted(d.items(), key=lambda x: x[0]):
    if len(a[1]) >= 2:
        print('%d %d ' % (a[0][0], a[0][1])+' '.join(a[1]))
