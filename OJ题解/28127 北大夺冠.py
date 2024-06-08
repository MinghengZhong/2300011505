from collections import defaultdict as D
a = D(set)
b = D(int)
for _ in range(int(input())):
    N, A, Y = input().split(',')
    b[N] += 1
    if Y == 'yes':
        a[N].add(A)
l = sorted(b.keys(), key=lambda x: (-len(a[x]), b[x], x))
for i in range(min(12, len(l))):
    print('%d %s %d %d' % (i+1, l[i], len(a[l[i]]), b[l[i]]))
