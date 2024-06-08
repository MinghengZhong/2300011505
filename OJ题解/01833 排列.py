import math
N = int(input())
for j in range(N):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    num = [i for i in range(1, n+1)]
    for i in range(0, n-1):
        m = num.index(l[i])
        k += m*math.factorial(n-i-1)
        num.pop(m)
    num = [i for i in range(1, n+1)]
    k %= math.factorial(n)
    for i in range(n-1, 0, -1):
        m = int(k//math.factorial(i))
        k = k % math.factorial(i)
        print(num[m], end=' ')
        num.pop(m)
    print(num[0])
