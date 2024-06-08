while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    elif m == 1:
        print(n)
        continue
    l = []
    for i in range(n):
        l.append(i+1)
    i = m-1
    while n > 1:
        if i > n-1:
            i = i % n
        n -= 1
        l.pop(i)
        i += m-1
    print(l[0])
