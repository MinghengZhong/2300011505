l = [0]*1000
for _ in range(int(input())):
    s = input().split()
    i = -1
    for a in s:
        if a == '+':
            l[i-1] += l[i]
            i -= 1
        elif a == '-':
            l[i-1] -= l[i]
            i -= 1
        elif a == '*':
            l[i-1] *= l[i]
            i -= 1
        elif a == '/':
            l[i-1] /= l[i]
            i -= 1
        else:
            i += 1
            l[i] = float(a)
    print('%.2f' % l[0])
