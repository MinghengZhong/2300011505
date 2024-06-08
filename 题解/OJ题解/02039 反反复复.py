n = int(input())
s = input()
m = len(s)//n
for i in range(n):
    for j in range(m):
        if j % 2 == 0:
            print(s[n*j+i], end='')
        else:
            print(s[n*(j+1)-i-1], end='')
