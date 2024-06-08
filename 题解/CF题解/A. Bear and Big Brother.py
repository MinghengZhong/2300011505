l = input().split()
a = int(l[0])
b = int(l[1])
ans = 0
while a <= b:
    a *= 3
    b *= 2
    ans += 1
print(ans)
