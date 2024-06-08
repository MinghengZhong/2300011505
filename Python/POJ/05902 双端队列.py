for _ in range(int(input())):
    l, i = [], 0
    for __ in range(int(input())):
        a, b = input().split()
        if a == '1':
            l.append(b)
        elif i < len(l):
            if b == '0':
                i += 1
            else:
                l.pop()
    print(' '.join(l[i:]) if i < len(l) else 'NULL')
