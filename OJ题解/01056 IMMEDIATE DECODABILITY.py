count = 0
while True:
    count += 1
    l = []
    used = []
    ans = True
    try:
        while True:
            s = input()
            if s == '9':
                break
            else:
                l.append(s)
        for s in l:
            a = ''
            for ss in s:
                a += ss
                if a in used:
                    ans = False
                    break
            if not ans:
                break
            used.append(s)
        if ans:
            print('Set %d is immediately decodable' % (count))
        else:
            print('Set %d is not immediately decodable' % (count))
    except EOFError:
        break
