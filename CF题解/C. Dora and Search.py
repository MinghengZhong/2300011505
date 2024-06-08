t = int(input())
for _ in range(t):
    n = int(input())
    big = list(map(int, input().split()))
    num = [0]+big
    big.sort()
    l = 1
    r = n
    s = 0
    b = n-1
    while True:
        if r == l:
            break
        else:
            if num[r] == big[s]:
                s += 1
                r -= 1
            elif num[r] == big[b]:
                b -= 1
                r -= 1
            elif num[l] == big[s]:
                s += 1
                l += 1
            elif num[l] == big[b]:
                b -= 1
                l += 1
            else:
                break
    if r == l:
        print(-1)
    else:
        print('%d %d' % (l, r))
