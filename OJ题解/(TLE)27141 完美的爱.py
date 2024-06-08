n = int(input())
l = [0]+list(map(int, input().split()))
s = [-1]
for i in range(1, n+1):
    l[i] += l[i-1]
    s += [l[i] % 520]
print(l)
print(s)
ans = 0
for i in range(0, n):
    for j in range(1, n+1):
        if (l[j]-l[i]) % 520 == 0:
            ans = max(ans, l[j]-l[i])
print(ans)
