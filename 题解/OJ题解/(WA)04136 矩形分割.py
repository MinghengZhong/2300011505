def f(x, l):
    d = 0
    for a, b, c in l:
        if a < x:
            d += (min(b, x)-a)*c
    return d


R = int(input())
l = []
s = 0
for _ in range(int(input())):
    L, T, W, H = map(int, input().split())
    l.append((L, L+W, H))
    s += H*W
i, j = 0, R
while j-i-1:
    m = (i+j)//2
    if f(m, l) <= s/2:
        i = m
    else:
        j = m
print(j if f(j, l) == s/2 else (i if f(i, l) == s/2 else j))
