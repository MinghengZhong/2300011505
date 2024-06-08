s = input()
s = input()
n = 0
for a in s:
    if a == 'A':
        n += 1
    else:
        n -= 1
if n > 0:
    print('Anton')
elif n < 0:
    print('Danik')
else:
    print('Friendship')
