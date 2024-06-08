n, m = map(int, input().split())
l = list(map(int, input().split()))
L = [[0]*(2 << i) for i in range(16)]
for a in l:
    for i in range(16):
        L[i][a % (2 << i)] += 1
for i in range(16):
    for j in range(1, 2 << i):
        L[i][j] += L[i][j-1]
d = 1
for _ in range(m):
    s, i = input().split()
    i = int(i)
    if s == 'C':
        d += i
    else:
        n = 2 << i
        l = (n//2-d) % n
        r = (n-d) % n
        print(L[i][r]-L[i][l] if r > l else L[i][-1]+L[i][r]-L[i][l])
