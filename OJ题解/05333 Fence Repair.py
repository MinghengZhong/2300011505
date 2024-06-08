from heapq import heappop, heappush
l = []
ans = 0
for _ in range(int(input())):
    heappush(l, int(input()))
while len(l)-1:
    a, b = heappop(l), heappop(l)
    ans += a+b
    heappush(l, a+b)
print(ans)
