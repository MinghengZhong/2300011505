s = input()
a = []
for i in range(0, len(s), 2):
    a.append(s[i])
a.sort()
for i in range(1, len(s), 2):
    a.insert(i, s[i])
for b in a:
    print(b, end='')
