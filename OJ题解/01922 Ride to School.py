while True:
    n = int(input())
    if n == 0:
        break
    ans = -1
    for i in range(n):
        v, t = map(int, input().split())
        if t >= 0:
            tt = t+16200/v
            if ans == -1:
                ans = tt
            elif tt < ans:
                ans = tt
    if int(ans) == ans:
        print(int(ans))
    else:
        print(int(ans)+1)
