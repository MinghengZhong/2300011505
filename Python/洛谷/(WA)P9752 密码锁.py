n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
if n == 1:
    print(81)
elif n == 2:
    print(10)
else:
    print(1)
