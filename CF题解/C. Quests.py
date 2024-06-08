t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans, count, maxb = 0, 0, 0
    for i in range(1, min(n, k)+1):
        count += a[i-1]
        maxb = max(maxb, b[i-1])
        ans = max(ans, count+(k-i)*maxb)
    print(ans)
