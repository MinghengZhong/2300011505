s = input()
if len(s) == 1:
    if s[0] < 'a':
        print(s[0].lower())
    else:
        print(s[0].upper())
else:
    n = True
    for i in range(1, len(s)):
        if s[i] >= 'a':
            n = False
    if s[0] >= 'a' and n:
        print(s[0].upper(), end='')
        for i in range(1, len(s)):
            print(s[i].lower(), end='')
    elif s[0] < 'a' and n:
        print(s.lower())
    else:
        print(s)
