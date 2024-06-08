from heapq import heappop, heappush


t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    l = sorted(list(map(int, input().split())))
    r = sorted(list(map(int, input().split())))
    c = sorted(list(map(int, input().split())), reverse=True)
    q, j = [], 0
    for i in range(n):
        while j < n and r[i] > l[j]:
            heappush(q, -l[j])
            j += 1
        r[i] += heappop(q)
    r.sort()
    for i in range(n):
        ans[_] += c[i]*r[i]
for a in ans:
    print(a)
