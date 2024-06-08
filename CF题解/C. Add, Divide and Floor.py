t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    a = min(l)
    b = max(l)
    if a == b:
        print(0)
    else:
        k = 0
        ans = ''
        while a != b:
            if a % 2 == 1:
                ans += '1'
                a += 1
                b += 1
            else:
                ans += '0'
            k += 1
            a //= 2
            b //= 2
        print(k)
        if k <= n:
            print(' '.join(ans))
