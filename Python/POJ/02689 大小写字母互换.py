s = input()
for i in range(0, len(s)):
    if 'a' <= s[i] <= 'z':
        print(s[i].upper(), end='')
    elif 'A' <= s[i] <= 'Z':
        print(s[i].lower(), end='')
    else:
        print(s[i], end='')
