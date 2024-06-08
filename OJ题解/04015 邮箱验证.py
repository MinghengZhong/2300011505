def check(s):
    if s[0] == '.' or s[0] == '@' or s[-1] == '.' or s[-1] == '@':
        return 'NO'
    at = False
    dot = False
    for i in range(1, len(s)-1):
        if s[i] == '@':
            if at:
                return 'NO'
            else:
                if s[i+1] == '.' or s[i-1] == '.':
                    return 'NO'
                else:
                    at = True
        elif s[i] == '.' and at:
            dot = True
    if dot and at:
        return 'YES'
    else:
        return 'NO'


while True:
    try:
        s = input()
        print(check(s))
    except EOFError:
        break
