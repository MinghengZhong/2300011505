while True:
    if (s := input()) == '.':
        break
    n = len(s)
    l = [0]*n
    for i in range(1, n):
        j = l[i-1]
        while j > 0 and s[i] != s[j]:
            j = l[j-1]
        if s[i] == s[j]:
            j += 1
        l[i] = j
    if l[-1] != 0 and n % (n-l[-1]) == 0:
        print(n//(n-l[-1]))
    else:
        print(1)
