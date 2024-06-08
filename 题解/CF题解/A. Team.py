n = int(input())
a = 0
for i in range(0, n):
    str = input()
    if int(str[0])+int(str[2])+int(str[4]) >= 2:
        a += 1
print(a)