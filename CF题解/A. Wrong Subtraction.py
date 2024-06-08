s = input().split()
n = int(s[0])
for i in range(0, int(s[1])):
    if n % 10 == 0:
        n /= 10
    else:
        n -= 1
print(int(n))
