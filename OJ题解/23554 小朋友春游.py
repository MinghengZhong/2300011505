n = int(input())
l = list(map(int, input().split()))
kid = [False]*(n+1)
y = []
x = []
for a in l:
    if a > n:
        x.append(a)
    elif kid[a]:
        x.append(a)
    else:
        kid[a] = True
for i in range(1, n+1):
    if not kid[i]:
        y.append(i)
print(' '.join(map(str, y)))
print(' '.join(map(str, sorted(x))))
