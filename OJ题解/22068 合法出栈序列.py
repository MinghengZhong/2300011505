S = input()
n = len(S)
d = {S[i]: i for i in range(n)}
while True:
    try:
        s = input()
    except EOFError:
        break
    f = len(s) != n
    for a in s:
        try:
            b = d[a]
        except KeyError:
            f = True
            break
    for i in range(n-1):
        if f:
            break
        a = d[s[i]]
        for j in range(i+1, n):
            b = d[s[j]]
            if b < d[s[i]]:
                if b < a:
                    a = b
                else:
                    f = True
                    break
    print('NO' if f else 'YES')
