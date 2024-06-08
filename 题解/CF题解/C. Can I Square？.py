from math import pow, sqrt

for _ in range(int(input())):
    n = int(input())
    l = sum(map(int, input().split()))
    if pow(int(sqrt(l)), 2) == l:
        print('YES')
    else:
        print('NO')
