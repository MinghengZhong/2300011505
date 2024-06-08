for _ in range(int(input())):
    n, f, a, b = map(int, input().split())
    l = [0]+sorted(list(map(int, input().split())))
    for i in range(n):
        f -= min(b, a*(l[i+1]-l[i]))
        if f <= 0:
            break
    if f <= 0:
        print('NO')
    else:
        print('YES')
