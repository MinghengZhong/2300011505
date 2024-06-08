n = int(input())
l = input().split()
a = 0
b = 0
c = 0
d = 0
ans = 0
for i in l:
    if i == '1':
        a += 1
    elif i == '2':
        b += 1
    elif i == '3':
        c += 1
    elif i == '4':
        d += 1
ans += d+int(b/2)+c
b = b % 2
if c >= a:
    a = 0
else:
    a -= c
ans += int(a/4)
a = a % 4
if a+2*b > 0 and a+2*b <= 4:
    ans += 1
elif a+2*b > 4:
    ans += 2
print(ans)
