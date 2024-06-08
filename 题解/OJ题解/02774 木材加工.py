n, k = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))
s = sum(l)
if s < k:
    print(0)
else:
    small, big = 1, max(l)
    while big-small > 1:
        middle = (small+big)//2
        count = 0
        for a in l:
            count += a//middle
        if count >= k:
            small = middle
        else:
            big = middle
    print(small)
