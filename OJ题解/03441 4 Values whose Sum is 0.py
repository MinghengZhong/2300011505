n = int(input())
L = [tuple(map(int, input().split())) for _ in range(n)]
D = {}
for a, _, _, _ in L:
    for _, b, _, _ in L:
        D[-a-b] = D.get(-a-b, 0)+1
ans = 0
for _, _, c, _ in L:
    for _, _, _, d in L:
        ans += D.get(c+d, 0)
print(ans)
