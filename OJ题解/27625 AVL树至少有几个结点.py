a = b = 1
for _ in range(int(input())):
    a, b = b, a+b
print(b-1)
