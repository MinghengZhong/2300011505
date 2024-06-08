n = int(input())
l = list(map(int, input().split()))
up = [1]*n
down = [1]*n
for i in range(1, n):
    for j in range(0, i):
        if l[i] > l[j]:
            up[i] = max(up[i], down[j]+1)
        elif l[i] < l[j]:
            down[i] = max(down[i], up[j]+1)
print(max(max(up), max(down)))
