import math


def operate(a, b, step):
    global ans
    if a == 1 or b == 1:
        if step < ans or ans == -1:
            ans = step
        return
    if step >= ans:
        return
    i = 2
    n = math.gcd(a, b)
    if n >= 2:
        j = -1
        while i <= n:
            if n % i == 0:
                j = i
                n //= i
            else:
                i += 1
        operate(a//j, b//j, step+1)
    operate(a-1, b-1, step+1)
    operate(a+1, b+1, step+1)
    return


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    ans = max(a, b)-1
    operate(a, b, 0)
    print(ans)
