n, m = map(int, input().split())
minl = []
maxl = []
maxs1 = ''
maxs2 = ''
maxi = -1
for i in range(n):
    s = ''.join(sorted(list(input())))
    minl.append(s)
    s = s[::-1]
    if maxs1 == '':
        maxi = i
        maxs1 = s
    elif maxs2 == '':
        if s < maxs1:
            maxs2 = maxs1
            maxs1 = s
            maxi = i
        else:
            maxs2 = s
    elif s < maxs1:
        maxs2 = maxs1
        maxs1 = s
        maxi = i
    elif maxs1 < s < maxs2:
        maxs2 = s
maxl.sort()
if n == 1:
    print(1)
else:
    for i in range(n):
        if i != maxi:
            if minl[i] < maxs1:
                print(1, end='')
            else:
                print(0, end='')
        else:
            if minl[i] < maxs2:
                print(1, end='')
            else:
                print(0, end='')
