s = input()
a = []
n = len(s)
for i in range(0, len(s)):
    if s[i] in a:
        n -= 1
    else:
        a.append(s[i])
if n % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
