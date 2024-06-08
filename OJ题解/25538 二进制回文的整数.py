n = int(input())
l = []
while n != 0:
    l += [n % 2]
    n = n//2
if l[::-1] == l:
    print('Yes')
else:
    print('No')
