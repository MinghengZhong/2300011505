from collections import defaultdict as D
l, r = D(lambda: []), D(lambda: [])


def mid(x):
    for a in sorted(l[x]):
        mid(a)
    print(x)
    for a in sorted(r[x]):
        mid(a)
    return


n = int(input())
not_root, is_root = set(), set()
for _ in range(n):
    L = list(map(int, input().split()))
    is_root.add(L[0])
    for i in range(1, len(L)):
        not_root.add(L[i])
        if L[i] < L[0]:
            l[L[0]].append(L[i])
        else:
            r[L[0]].append(L[i])
for a in is_root:
    if a not in not_root:
        mid(a)