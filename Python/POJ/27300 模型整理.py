from collections import defaultdict


def v(s):
    n = float(s[:-1])
    if s[-1] == 'B':
        n *= 1000
    return n


d = defaultdict(lambda: [])
for _ in range(int(input())):
    a, b = input().split('-')
    d[a].append(b)
for a in sorted(list(d.keys())):
    print('%s: %s' % (a, ', '.join(sorted(d[a], key=lambda i: v(i)))))
