from heapq import heappush, heappop


for _ in range(int(input())):
    m, n = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    for i in range(m-1):
        b = sorted(list(map(int, input().split())))
        c = []
        for x in b:
            for y in a:
                if len(c) < n:
                    heappush(c, -x-y)
                else:
                    if -x-y <= c[0]:
                        break
                    heappop(c)
                    heappush(c, -x-y)
        a = [-heappop(c) for j in range(n)][::-1]
    print(*a)
