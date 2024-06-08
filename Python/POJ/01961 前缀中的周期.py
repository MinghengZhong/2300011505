t = 0
while t := t+1:
    if (n := int(input())) == 0:
        break
    s = input()
    n = len(s)
    l = [0]*n
    for i in range(1, n):
        j = l[i-1]
        while j > 0 and s[i] != s[j]:
            j = l[j-1]
        if s[i] == s[j]:
            j += 1
        l[i] = j
    print('Test case #%d' % t)
    for i in range(1, n+1):
        if l[i-1] != 0 and i % (i-l[i-1]) == 0:
            print(i, i//(i-l[i-1]))
    print()
