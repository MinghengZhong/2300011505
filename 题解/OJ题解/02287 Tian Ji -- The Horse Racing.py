while True:
    n = int(input())
    if n == 0:
        break
    l1 = sorted(list(map(int, input().split())), reverse=True)
    l2 = sorted(list(map(int, input().split())), reverse=True)
    win, i1, i2, j1, j2 = 0, 0, 0, n-1, n-1
    while (i1 <= j1):
        if l1[i1] > l2[i2]:
            i1 += 1
            i2 += 1
            win += 1
        else:
            if l1[j1] > l2[j2]:
                j1 -= 1
                j2 -= 1
                win += 1
            else:
                if l1[j1] < l2[i2]:
                    win -= 1
                j1 -= 1
                i2 += 1
    print(win*200)
