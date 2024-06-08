s = input()
low = 0
for i in range(0, len(s)):
    if s[i] > 'Z':
        low += 1
low *= 2
if low >= len(s):
    print(s.lower())
else:
    print(s.upper())
