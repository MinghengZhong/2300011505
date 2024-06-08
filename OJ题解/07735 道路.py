from heapq import heappop, heappush
K = int(input())
N = int(input())
g = [[] for _ in range(N)]
for _ in range(int(input())):
    S, D, L, T = map(int, input().split())
    g[S-1].append((D-1, L, T))
q = []
heappush(q, (0, 0, 0, 0))
while q:
    x, y, n, a = heappop(q)
    if a == N-1:
        print(x)
        exit()
    for b, l, t in g[a]:
        if n+1 < N and y+t <= K:
            heappush(q, (x+l, y+t, n+1, b))
print(-1)
