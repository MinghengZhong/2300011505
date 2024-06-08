from heapq import heappush, heappop

for _ in range(int(input())):
    l = list(map(int, input().split()))
    small, big, a = [], [], [l[0]]
    r = 0
    mid = l[0]
    c = 1
    for x in l[1:]:
        c += 1
        if x >= mid:
            heappush(big, x)
            r += 1
        else:
            heappush(small, -x)
            r -= 1
        if c % 2:
            if r == 2:
                heappush(small, -mid)
                mid = heappop(big)
                r = 0
            if r == -2:
                heappush(big, mid)
                mid = -heappop(small)
                r = 0
            a.append(mid)
    print(len(a))
    print(' '.join(map(str, a)))
