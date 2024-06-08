while True:
    n, m = map(int, input().split())
    if m == n == 0:
        break
    elif m == n:
        print(0)
        print('')
        continue
    l = [n]
    anss = ['']*2500000
    start, end = 0, 0
    ans = 1
    flag = False
    while end != len(l):
        start, end = end, len(l)
        for i in range(start, end):
            nn = l[i]
            if nn*3 < len(anss) and not anss[nn*3]:
                anss[nn*3] = anss[nn]+'H'
                l.append(nn*3)
                if nn*3 == m:
                    flag = True
                    break
            if nn//2 > 0 and not anss[nn//2]:
                anss[nn//2] = anss[nn]+'O'
                l.append(nn//2)
                if nn//2 == m:
                    flag = True
                    break
        if flag:
            break
        ans += 1
    print(ans)
    print(anss[m])
