s = input().split()
n = int(s[0])
k = int(s[1])
if 2*k-1 <= n:
    print(2*k-1)
else:
    if n % 2 == 0:
        print(2*(k-int(n/2)))
    else:
        print(2*(k-int(n/2)-1))
