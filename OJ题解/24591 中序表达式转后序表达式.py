for _ in range(int(input())):
    t, l, s, A = '', [], [], []
    p = {'+': 0, '-': 0, '*': 1, '/': 1}
    for a in input().strip():
        if '0' <= a <= '9' or a == '.':
            t += a
        else:
            if t:
                l.append(t)
                t = ''
            l.append(a)
    if t:
        l.append(t)
    for a in l:
        try:
            b = float(a)
            A.append(a)
        except ValueError:
            if a == '(':
                s.append(a)
            elif a == ')':
                while s and s[-1] != '(':
                    A.append(s.pop())
                s.pop()
            else:
                while s and s[-1] != '(' and p[s[-1]] >= p[a]:
                    A.append(s.pop())
                s.append(a)
    while s:
        A.append(s.pop())
    print(' '.join(A))
