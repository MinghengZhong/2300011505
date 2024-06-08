import heapq as H
n = int(input())
l = list(map(int, input().split()))
ans = 0
H.heapify(l)
for _ in range(n-1):
    a = H.heappop(l)
    b = H.heappop(l)
    ans += a+b
    H.heappush(l, a+b)
print(ans)
