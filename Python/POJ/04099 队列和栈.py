for _ in range(int(input())):
    q, s, j, f = [], [], 0, False
    for i in range(int(input())):
        l = input()
        if f:
            continue
        if l[1] == 'o':
            if j == len(q):
                f = True
            else:
                j += 1
                s.pop()
        else:
            a = l.split()[1]
            q.append(a)
            s.append(a)
    if f:
        print('error\nerror')
    else:
        print(' '.join(q[j:])+'\n'+' '.join(s))
