s = input().split('+')
ans = 0
for a in s:
    b = a.split('^')
    if b[0] != '0n':
        if int(b[1]) > ans:
            ans = int(b[1])
print('n^%d' % ans)
