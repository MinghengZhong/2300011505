from collections import defaultdict as D
d = D(lambda: set())
n = int(input())
for i in range(n):
    for a in list(map(int, input().split()))[1:]:
        d[a].add(i)
for i in range(int(input())):
    l = list(map(int, input().split()))
    g = list(d.keys())
    f = [True]*len(g)
    for j, a in enumerate(g):
        if f[j]:
            for k in range(n):
                if l[k] == 1:
                    if k not in d[a]:
                        f[j] = False
                elif l[k] == -1:
                    if k in d[a]:
                        f[j] = False
    ans = [g[j] for j in range(len(f)) if f[j]]
    print(' '.join(map(str, sorted(ans))) if ans else 'NOT FOUND')
