s = input().split()
n = int(s[0])
t = int(s[1])
s = input()
l = []
b = True
for a in s:
    l.append(a)
for i in range(0, t):
    for j in range(1, n):
        if l[j] == 'G' and l[j-1] == 'B' and b:
            l[j] = 'B'
            l[j-1] = 'G'
            b = False
        else:
            b = True
    b = True
for i in range(0, n):
    print(l[i], end='')
