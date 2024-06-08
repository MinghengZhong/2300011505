n = int(input())
if n % 4 == 0:
    print(str(int(n/4))+' '+str(int(n/2)))
elif n % 2 == 0:
    print(str(int(n/4)+1)+' '+str(int(n/2)))
else:
    print('0 0')
