for _ in range(int(input())):
    x, y = {}, {}
    for i in range(4):
        a, b = map(int, input().split())
        x[a] = 0
        y[b] = 0
    x1, x2 = x.keys()
    y1, y2 = y.keys()
    print(abs((x1-x2)*(y1-y2)))
