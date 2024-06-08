while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    l = list(map(int, input().split()))
    a = 0
    for i in range(n):
        for j in range(1, l[n+i]+1):
            a = (a | ((a | 1) << l[i]*j)) % (1 << (m+1))
    ans = 0
    while a > 0:
        ans += a % 2
        a >>= 1
    print(ans-1)
