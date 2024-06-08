n, l = map(int, input().split())
l = list(map(int, input().split()))
t = n*2
c = [0, 0, 0, 0]
ans = True
for i in l:
    n -= i//4
    c[i % 4] += 1
n -= c[3]
if n < 0:
    t += 2*n
    n = 0
if t < 0:
    ans = False
elif t > c[2]:
    c[1] = max(c[1]-t+c[2], 0)
    c[2] = 0
else:
    c[2] -= t
a = abs(c[1]-c[2])
if c[1] > c[2]:
    if c[2]+a//2+a % 2 > n:
        ans = False
else:
    if c[1]+(a//3)*2+a % 3 > n:
        ans = False
if ans:
    print('YES')
else:
    print('NO')
