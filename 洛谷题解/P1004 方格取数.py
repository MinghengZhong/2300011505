N = int(input())
n = 0
x = []
y = []
num = []
next = []
used = []
ans = 0


def pick(n, count, first):
    global used, next, ans
    if count > ans:
        ans = count
    for i in next[n]:
        if not used[i]:
            used[i] = True
            pick(i, count+num[i], first)
            used[i] = False
    if first:
        for i in range(n):
            if not used[i]:
                used[i] = True
                pick(i, count+num[i], False)
                used[i] = False


while True:
    xi, yi, numi = map(int, input().split())
    if xi == 0:
        break
    x.append(xi)
    y.append(yi)
    num.append(numi)
    next.append([])
    used.append(False)
    for i in range(n):
        if x[i] >= xi and y[i] >= yi:
            next[n].append(i)
        elif xi >= x[i] and yi >= y[i]:
            next[i].append(n)
    n += 1
for i in range(n):
    used[i] = True
    pick(i, num[i], True)
    used[i] = False
print(ans)
