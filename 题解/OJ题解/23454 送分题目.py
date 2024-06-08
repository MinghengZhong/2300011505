s = input().split()
print(s[0], end='')
for i in range(1, len(s)):
    print(' %s' % s[i], end='')
