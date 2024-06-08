a, b, k = map(int, input().split())
bomb = []
ans = 0
for _ in range(a):
    bomb.append([True]*b)
for _ in range(k):
    x, y, r, t = map(int, input().split())
    x -= 1
    y -= 1
    r = r//2
    if t == 1:
        for i in range(a):
            for j in range(b):
                if abs(i-x) > r or abs(j-y) > r:
                    bomb[i][j] = False
    else:
        for i in range(x-r, x+r+1):
            for j in range(y-r, y+r+1):
                if i >= 0 and j >= 0 and i < a and j < b:
                    bomb[i][j] = False
for i in range(a):
    for j in range(b):
        if bomb[i][j]:
            ans += 1
print(ans)
