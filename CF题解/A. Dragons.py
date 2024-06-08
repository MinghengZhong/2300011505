sss = input().split()
s = int(sss[0])
n = int(sss[1])
x = []
y = {}
for i in range(0, n):
    sss = input().split()
    if int(sss[0]) not in x:
        x.append(int(sss[0]))
    if int(sss[0]) in y:
        y[int(sss[0])] += int(sss[1])
    else:
        y[int(sss[0])] = int(sss[1])
x.sort()
win = 'YES'
for i in x:
    if s > i:
        s += y[i]
    else:
        win = 'NO'
        break
print(win)
