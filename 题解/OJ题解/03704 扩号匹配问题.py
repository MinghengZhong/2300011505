while True:
    try:
        s = input()
    except EOFError:
        break
    n = len(s)
    a, l = [' ']*n, []
    for i in range(n):
        if s[i] == '(':
            l.append(i)
        elif s[i] == ')':
            if l:
                l.pop()
            else:
                a[i] = '?'
    for i in l:
        a[i] = '$'
    print(s+'\n'+''.join(a))
