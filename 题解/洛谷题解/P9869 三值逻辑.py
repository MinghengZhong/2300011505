def op(s):
    if s == 'F':
        return 'T'
    elif s == 'T':
        return 'F'
    elif s == 'U':
        return 'U'
    elif s[0] == '-':
        return s[1:]
    else:
        return '-'+s


c, t = map(int, input().split())
for _ in range(t):
    n, m = map(int, input().split())
    l = [str(i) for i in range(n+1)]
    mustU = [False]*(n+1)
    for __ in range(m):
        s = input()
        if s[0] == '+' or s[0] == '-':
            v, i, j = s.split()
            i = int(i)
            j = int(j)
            if v == '+':
                l[i] = l[j]
            elif v == '-':
                l[i] = op(l[j])
        else:
            v, i = s.split()
            i = int(i)
            l[i] = v
    for i in range(1, n+1):
        if l[i] == 'U' or l[i] == '-'+str(i) or str(i) == '-'+l[i]:
            mustU[i] = True
    b = True
    while b:
        b = False
        for i in range(1, n+1):
            if not mustU[i]:
                if '1' <= l[i][0] <= '9':
                    if mustU[int(l[i])]:
                        mustU[i] = True
                        b = True
                elif l[i][0] == '-':
                    if mustU[int(l[i][1:])]:
                        mustU[i] = True
                        b = True
    ans = 0
    for i in mustU:
        if i:
            ans += 1
    print(ans)
