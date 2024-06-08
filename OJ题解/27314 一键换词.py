l = input().split()
s1, s2 = input().split()
s1, s2 = s1.lower(), s2.lower()
cap = True
for i in range(len(l)):
    s = l[i]
    b = False
    c = False
    if s[-1] == '.':
        s = s[:-1]
        b = True
    if s[-1] == ',':
        s = s[:-1]
        c = True
    s = s.lower()
    if s == s1:
        s = s2
    if cap:
        cap = False
        s = s.capitalize()
    print(s, end='')
    if b:
        cap = True
        print('.', end='')
    if c:
        print(',', end='')
    if i != len(l)-1:
        print(' ', end='')
    else:
        print('')
