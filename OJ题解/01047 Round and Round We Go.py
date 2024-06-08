def compare(sa, b):
    sb = str(b)
    if len(sb) > len(sa):
        return False
    elif len(sb) < len(sa):
        sb = '0'*(len(sa)-len(sb))+sb
    for i in range(0, len(sa)):
        if sa[0:i+1] not in sb:
            if i == 0:
                return False
            else:
                sa = sa[i:]+sa[0:i]
                break
    return sa == sb


while True:
    try:
        sn = input()
        n = int(sn)
        if n == 0:
            print(sn+' is cyclic')
            continue
        elif int(sn[0]) >= 5:
            print(sn+' is not cyclic')
            continue
        j = 2
        ans = ''
        for i in range(2, len(sn)+1):
            if not compare(sn, n*j):
                ans = 'not '
                break
            j += 1
        print(sn+' is '+ans+'cyclic')
    except EOFError:
        break
