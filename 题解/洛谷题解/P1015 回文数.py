def add(ll, N):
    n = len(ll)
    l = [ll[i]+ll[n-i-1] for i in range(n)]
    for i in range(n-1):
        if l[i] >= N:
            l[i+1] += l[i]//N
            l[i] = l[i] % N
    if l[n-1] >= N:
        l.append(l[n-1]//N)
        l[n-1] = l[n-1] % N
    return l[::-1]


def check(l):
    n = len(l)
    for i in range(n//2):
        if l[i] != l[n-i-1]:
            return False
    return True


num = ('0', '1', '2', '3', '4', '5', '6', '7',
       '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


N = int(input())
l = list(map(num.index, input()[:-1]))
for i in range(31):
    if check(l):
        print('STEP={}'.format(i))
        break
    elif i == 30:
        print('Impossible!')
    else:
        l = add(l, N)
