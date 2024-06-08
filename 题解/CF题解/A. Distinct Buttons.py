t = int(input())
ans = [False]*t
for _ in range(t):
    n = int(input())
    left, right, up, down = 0, 0, 0, 0
    for i in range(n):
        a, b = map(int, input().split())
        if a > 0:
            right = 1
        elif a < 0:
            left = 1
        if b > 0:
            up = 1
        elif b < 0:
            down = 1
    if left+right+up+down <= 3:
        ans[_] = True
for a in ans:
    if a:
        print('YES')
    else:
        print('NO')
