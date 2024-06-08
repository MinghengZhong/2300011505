a = []
while True:
    l = list(map(int, input().split()))
    empty = True
    for i in l:
        if i != 0:
            empty = False
    if empty:
        break
    ans = l[5]
    if l[0] >= l[4]*11:
        ans += l[4]
        l[0] -= l[4]*11
    else:
        ans += l[4]
        l[0] = 0
    if l[1] >= l[3]*5:
        ans += l[3]
        l[1] -= l[3]*5
    elif l[1]*4+l[0] >= l[3]*20:
        ans += l[3]
        l[0] -= l[3]*20-l[1]*4
        l[1] = 0
    else:
        ans += l[3]
        l[1] = 0
        l[0] = 0
    ans += int(l[2]/4)+int(l[1]/9)+int(l[0]/36)
    l[2] %= 4
    l[1] %= 9
    l[0] %= 36
    if l[2] == 1:
        ans += 1
        if l[1] >= 5:
            l[1] -= 5
            if l[0] >= 7:
                l[0] -= 7
            else:
                l[0] = 0
        else:
            if 27-4*l[1] >= l[0]:
                l[1] = 0
                l[0] = 0
            else:
                l[0] -= 27-4*l[1]
                l[1] = 0
    elif l[2] == 2:
        ans += 1
        if l[1] >= 3:
            l[1] -= 3
            if l[0] >= 6:
                l[0] -= 6
            else:
                l[0] = 0
        else:
            if 18-4*l[1] >= l[0]:
                l[1] = 0
                l[0] = 0
            else:
                l[0] -= 18-4*l[1]
                l[1] = 0
    elif l[2] == 3:
        ans += 1
        if l[1] >= 1:
            l[1] -= 1
            if l[0] >= 5:
                l[0] -= 5
            else:
                l[0] = 0
        else:
            if 9 >= l[0]:
                l[0] = 0
            else:
                l[0] -= 9
    if l[0]+4*l[1] > 36:
        ans += 2
    elif 0 < l[0]+4*l[1] <= 36:
        ans += 1
    a.append(ans)
for ans in a:
    print(ans)
