x, y, m, n, L = map(int, input().split())
d, l, ans = (m-n) % L, (x-y) % L, 0
s = set()
while True:
    if l in s:
        print('Impossible')
        break
    elif l == 0:
        print(ans)
        break
    s.add(l)
    l = (l+d) % L
    ans += 1
