cases = 0
while True:
    cases += 1
    a, b, c, d = map(int, input().split())
    if a == -1:
        break
    a %= 23
    b %= 28
    c %= 33
    for i in range(1, 21253):
        if i % 23 == a and i % 28 == b and i % 33 == c:
            if i > d:
                ans = i-d
            else:
                ans = i+21252-d
            break
    print('Case '+str(cases)+': the next triple peak occurs in '+str(ans)+' days.')
