s = input()
if s[0] <= 'z':
    if len(s) == 1:
        print(s[0].upper())
    else:
        print(s[0].upper()+s[1:])
else:
    print(s)
