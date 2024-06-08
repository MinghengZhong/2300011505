n = int(input())
s = input().split()
b = False
for i in range(0, n):
    if s[i] == '1':
        b = True
        break
if b:
    print('HARD')
else:
    print('EASY')
