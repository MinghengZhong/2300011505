s = input()
c = 0
l = ['h', 'e', 'l', 'l', 'o', '012']
for i in range(0, len(s)):
    if s[i] == l[c]:
        c += 1
if c == 5:
    print('YES')
else:
    print('NO')