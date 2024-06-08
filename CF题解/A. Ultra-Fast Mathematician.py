a = input()
b = input()
for i in range(0, len(a)):
    if a[i] != b[i]:
        print('1', end='')
    else:
        print('0', end='')
