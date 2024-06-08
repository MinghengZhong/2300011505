s = input()
n = 1
b = False
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        n += 1
    else:
        n = 1
    if n == 7:
        b = True
        break
if b:
    print('YES')
else:
    print('NO')
