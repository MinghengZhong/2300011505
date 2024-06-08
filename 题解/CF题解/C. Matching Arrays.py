t = int(input())
ans = [True]*t
anss = []
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

i = 0
for a in ans:
    if a:
        print('YES')
        print(anss[i])
        i += 1
    else:
        print('NO')
