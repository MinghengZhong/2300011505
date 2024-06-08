t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    count, c = 0, {}
    while len(c) != 2:
        c = {}
        count += 1
        for i in range(n):
            c[l[i] % 2] = 0
            l[i] //= 2
    ans[_] = 2**count
for a in ans:
    print(a)
