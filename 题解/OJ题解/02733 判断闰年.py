n = int(input())
if n % 100 == 0:
    if n % 400 == 0:
        print('Y')
    else:
        print('N')
elif n % 4 == 0:
    print('Y')
else:
    print('N')
