s = input().split()
n = int(s[0])
m = int(s[1])
a = int(s[2])
if m % a != 0:
    m = int(m/a)*a+a
if n % a != 0:
    n = int(n/a)*a+a
print(int(m*n/a/a))
