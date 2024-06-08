from math import sqrt

step = 0
while True:
    step += 1
    n, d = map(int, input().split())
    if n == d == 0:
        break
    l = [(0, 0)]*n
    used = [False]*n
    b = False
    for i in range(n):
        x, y = map(int, input().split())
        if y > d:
            b = True
        else:
            l[i] = (x-sqrt(d**2-y**2), x+sqrt(d**2-y**2))
    s = input()
    if b:
        print('Case %d: -1' % step)
        continue
    ans = 0
    l.sort(key=lambda x: x[1])
    for i in range(n):
        if not used[i]:
            ans += 1
            used[i] = True
            for j in range(i+1, n):
                if l[j][0] <= l[i][1] and not used[j]:
                    used[j] = True
    print('Case %d: %d' % (step, ans))
