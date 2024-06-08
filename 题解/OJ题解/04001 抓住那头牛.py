n, k = map(int, input().split())
if n >= k:
    print(n-k)
else:
    l, f = [n], set([n])
    s, e, x = 0, 1, 0
    while True:
        if k in f:
            print(x)
            exit()
        x += 1
        for i in range(s, e):
            a = l[i]
            for j in (a-1, a+1, a+a):
                if 0 <= j <= 1e5 and j not in f:
                    l.append(j)
                    f.add(j)
        s, e = e, len(l)
