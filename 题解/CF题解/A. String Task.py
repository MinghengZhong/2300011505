s = input().lower()
c = ['a', 'e', 'i', 'o', 'u', 'y']
for i in range(0, len(s)):
    if s[i] not in c:
        print('.'+s[i], end='')
