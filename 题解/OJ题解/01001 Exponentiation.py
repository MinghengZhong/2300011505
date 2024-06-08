while True:
    try:
        s = input().split()
        n = int(s[1])
        r = 0
        dot = 0
        for i in range(0, 6):
            if s[0][i] == '.':
                dot = 5-i
                dott = 5-i
            else:
                r = r*10+int(s[0][i])
        l = list(str(r**n))
        dot *= n
        dott *= n
        while l[-1] == '0':
            l.pop()
            dot -= 1
        if dot <= 0:
            print(str(int((r**n)/(10**dott))))
        else:
            if dot >= len(l):
                print('.', end='')
                for i in range(0, dot-len(l)):
                    print('0', end='')
                for a in l:
                    print(a, end='')
            else:
                l.insert(-dot, '.')
                for a in l:
                    print(a, end='')
            print('')
    except EOFError:
        break
