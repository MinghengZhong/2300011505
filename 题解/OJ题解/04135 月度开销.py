def check(l, m, k):
    count = 0
    for a in l:
        if count+a > k:
            m -= 1
            count = 0
        count += a
    return m >= 1


n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(int(input()))
left, right = max(l)-1, sum(l)
while right-left > 1:
    middle = (left+right)//2
    if check(l, m, middle):
        right = middle
    else:
        left = middle
print(right)
