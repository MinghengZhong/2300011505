def cal(s):
    A = B = e = k = ''
    i = 0
    while i != len(s):
        a = s[i]
        if a in '&|':
            e = a
        if a == '!':
            k = '' if k else a
        if a == '(':
            l, n = '', 1
            while n:
                i += 1
                if s[i] == ')':
                    n -= 1
                elif s[i] == '(':
                    n += 1
                if n:
                    l += s[i]
            a = cal(l)
        if a in 'VF':
            if k:
                if A:
                    B = 'V' if a == 'F' else 'F'
                else:
                    A = 'V' if a == 'F' else 'F'
                k = ''
            else:
                if A:
                    B = a
                else:
                    A = a
        if A and B and e:
            if e == '&':
                A = 'V' if A == B == 'V' else 'F'
            elif e == '|':
                A = 'F' if A == B == 'F' else 'V'
            B = e = ''
        i += 1
    return A


while True:
    try:
        print(cal(input()))
    except EOFError:
        break
