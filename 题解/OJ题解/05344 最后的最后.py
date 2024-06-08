n, k = map(int, input().split())
l = []
next = [i+1 for i in range(n+1)]
next[-1] = 1
i = 0
for _ in range(n-1):
    for j in range(k-1):
        i = next[i]
    l.append(next[i])
    next[i] = next[next[i]]
print(' '.join(map(str, l)))
