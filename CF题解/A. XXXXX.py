t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    count = 0
    ans = False
    for a in l:
        if a % x != 0:
            ans = True
        count += a % x
    if ans:
        if count % x == 0:
            for j in range(1, n):
                if l[j-1] % x != 0 or l[n-j] % x != 0:
                    n -= j
                    break
        print(n)
    else:
        print('-1')
