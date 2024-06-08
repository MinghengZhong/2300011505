n = int(input())
x = 0
y = 0
z = 0
for i in range(0, n):
    s = input().split()
    x += int(s[0])
    y += int(s[1])
    z += int(s[2])
if x == 0 and y == 0 and z == 0:
    print('YES')
else:
    print('NO')
