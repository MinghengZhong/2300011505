while True:
    n, p, k = map(int, input().split())
    if n == 0:
        break
    l = []
    next = [i+1 for i in range(n+1)]
    next[-1] = 1
    i = p-1
    for _ in range(n):
        for j in range(k-1):
            i = next[i]
        l.append(next[i])
        next[i] = next[next[i]]
    print(','.join(map(str, l)))
