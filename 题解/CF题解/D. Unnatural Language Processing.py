for _ in range(int(input())):
    n = int(input())
    s = input()
    c = {'a': False, 'b': True, 'c': True, 'd': True, 'e': False}
    i = 0
    while i < len(s)-1:
        print(s[i]+s[i+1], end='')
        i += 2
        if i >= len(s):
            break
        if i == len(s)-1:
            print(s[i], end='')
            i += 1
        elif c[s[i+1]]:
            print(s[i], end='.')
            i += 1
        else:
            print('.', end='')
    print('')
