d = int(input())
n = int(input())
M = [[0]*1025 for i in range(1025)]
MAX = 0
maxx = 0
maxy = 0
ans = 0
for _ in range(n):
    x, y, a = map(int, input().split())
    maxx = max(x, maxx)
    maxy = max(y, maxy)
    for i in range(max(0, y-d), min(1024, y+d)+1):
        for j in range(max(0, x-d), min(1024, x+d)+1):
            M[i][j] += a
            MAX = max(MAX, M[i][j])
for i in range(0, min(1024, maxy+d)+1):
    for j in range(0, min(1024, maxx+d)+1):
        if M[i][j] == MAX:
            ans += 1
print('%d %d' % (ans, MAX))
