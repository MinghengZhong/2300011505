x = []
h = []
n = int(input())
ans = 0


def cut(i, count, left, right):
    global x, h, n, ans
    if i == n:
        if count > ans:
            ans = count
        return
    canleft = True
    canright = True
    for j in x:
        if x[i]-h[i] <= j < x[i]:
            canleft = False
            break
    for j in x:
        if x[i] < j <= x[i]+h[i]:
            canright = False
            break
    if canleft:
        for j in range(count):
            if not (left[j] > x[i] or right[j] < x[i]-h[i]):
                canleft = False
                break
    if canright:
        for j in range(count):
            if not (left[j] > x[i]+h[i] or right[j] < x[i]):
                canright = False
                break
    if canleft:
        cut(i+1, count+1, left+[x[i]-h[i]], right+[x[i]])
    if canright:
        cut(i+1, count+1, left+[x[i]], right+[x[i]+h[i]])
    cut(i+1, count, left, right)
    return


for i in range(n):
    xi, hi = map(int, input().split())
    x.append(xi)
    h.append(hi)
cut(0, 0, [], [])
print(ans)