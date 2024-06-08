for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())))
    ans = 0
    l1, r1, l2, r2 = 0, n-1, 0, m-1
    while True:
        left = abs(b[l2]-a[l1])
        right = abs(b[r2]-a[r1])
        if l1 == r1:
            ans += max(left, right)
            break
        if left > right:
            ans += left
            l1 += 1
            l2 += 1
        else:
            ans += right
            r1 -= 1
            r2 -= 1
    print(ans)
