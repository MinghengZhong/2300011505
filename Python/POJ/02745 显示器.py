l1 = [1, 0, 1, 1, 0, 1, 1, 1, 1, 1]
l2 = [1, 0, 0, 0, 1, 1, 1, 0, 1, 1]
r2 = [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
l3 = [0, 0, 1, 1, 1, 1, 1, 0, 1, 1]
l4 = [1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
r4 = [1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
l5 = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
l = [' ', '-']
r = [' ', '|']
while True:
    s, inputl = input().split()
    if s == '0':
        break
    s = int(s)
    n = len(inputl)
    ll = list(map(int, inputl))
    for a in range(n):
        print(' '+l[l1[ll[a]]]*s+' ', end='')
        if a != n-1:
            print(' ', end='')
    print('')
    for i in range(s):
        for a in range(n):
            print(r[l2[ll[a]]]+' '*s+r[r2[ll[a]]], end='')
            if a != n-1:
                print(' ', end='')
        print('')
    for a in range(n):
        print(' '+l[l3[ll[a]]]*s+' ', end='')
        if a != n-1:
            print(' ', end='')
    print('')
    for i in range(s):
        for a in range(n):
            print(r[l4[ll[a]]]+' '*s+r[r4[ll[a]]], end='')
            if a != n-1:
                print(' ', end='')
        print('')
    for a in range(n):
        print(' '+l[l5[ll[a]]]*s+' ', end='')
        if a != n-1:
            print(' ', end='')
    print('')
    print('')
