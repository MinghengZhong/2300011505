def comparee(s1, s2):
    ii1 = 0
    ii2 = 0
    stop = False
    while True:
        if ii1 == len(s1) and ii2 == len(s2):
            return True
        elif ii2 == len(s2):
            if stop:
                return False
            else:
                return True
        if s1[ii1] != s2[ii2]:
            if stop:
                return False
            else:
                stop = True
                ii1 += 1
        else:
            ii1 += 1
            ii2 += 1


def compare(s1, s2):
    if len(s1)-len(s2) >= 2 or len(s2)-len(s1) >= 2:
        return False
    elif len(s1) == len(s2) and len(s1) == 1:
        return True
    elif len(s1) == len(s2):
        stop = False
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                if stop:
                    return False
                else:
                    stop = True
        return True
    elif len(s1)-len(s2) == 1:
        return comparee(s1, s2)
    else:
        return comparee(s2, s1)


dic = []
while True:
    s = input()
    if s == '#':
        break
    dic.append(s)
words = []
while True:
    s = input()
    if s == '#':
        break
    words.append(s)
for word in words:
    if word in dic:
        print(word+' is correct')
    else:
        print(word+':', end='')
        for dicw in dic:
            if compare(word, dicw):
                print(' '+dicw, end='')
        print('')
