n = int(input())
print('I hate', end=' ')
for i in range(0,n-1):
    if i % 2 == 0:
        print('that I love', end=' ')
    else:
        print('that I hate', end=' ')
print('it')
