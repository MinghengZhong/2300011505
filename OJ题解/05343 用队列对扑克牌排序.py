n = input()
d = [[] for _ in range(10)]
D = {s: [] for s in 'ABCD'}
A = []
for s in input().split():
    d[int(s[1])].append(s)
for i in range(1, 10):
    print('Queue%d:' % i+' '.join(d[i]))
    for s in d[i]:
        D[s[0]].append(s)
for a in D.items():
    print('Queue%s:' % a[0]+' '.join(a[1]))
    A += a[1]
print(' '.join(A))
