while True:
    N = int(input())
    if N == 0:
        break
    ans, l, s = 0, [], set()
    for i in range(N):
        l.append([i]+list(map(int, input().split())))
    l.sort(key=lambda a: a[1])
    s.add(l[0][0])
    temp, cheap = l[0][2], 10001
    for i in range(1, N):
        if l[i][1] != l[i-1][1]:
            cheap = min(cheap, temp)
            temp = 10001
        if cheap > l[i][2]:
            s.add(l[i][0])
        temp = min(temp, l[i][2])
    l.sort(key=lambda a: a[2])
    if l[0][0] in s:
        ans += 1
    temp, cheap = l[0][1], 10001
    for i in range(1, N):
        if l[i][2] != l[i-1][2]:
            cheap = min(cheap, temp)
            temp = 10001
        if cheap > l[i][1]:
            if l[i][0] in s:
                ans += 1
        temp = min(temp, l[i][1])
    print(ans)
