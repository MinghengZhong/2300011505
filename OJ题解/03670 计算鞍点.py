l = []
biggest = []
smallest = []
for i in range(5):
    inp = list(map(int, input().split()))
    biggest.append(inp.index(max(inp)))
    l.append(inp)
for j in range(5):
    small = -1
    for k in range(5):
        if l[k][j] <= small or small == -1:
            small = l[k][j]
            smallk = k
    smallest.append(smallk)
ansx = 0
ansy = 0
for i in range(5):
    if smallest[biggest[i]] == i:
        ansx = i+1
        ansy = biggest[i]+1
if ansx == ansy == 0:
    print('not found')
else:
    print('%d %d %d' % (ansx, ansy, l[ansx-1][ansy-1]))
