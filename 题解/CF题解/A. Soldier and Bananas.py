s = input().split()
k = int(s[0])
n = int(s[1])
w = int(s[2])
c = int(k*w*(w+1)/2)
if c <= n:
    print(0)
else:
    print(c-n)
