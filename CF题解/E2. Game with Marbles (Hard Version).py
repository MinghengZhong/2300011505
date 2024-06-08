t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l = [(0, 0)]*n
    for i in range(n):
        l[i] = (a[i], b[i])
    l.sort(key=lambda x: x[0]+x[1], reverse=True)
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += l[i][0]-1
        else:
            ans -= l[i][1]-1
    print(ans)
