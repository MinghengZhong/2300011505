x = []
h = []
left = []
right = []
cut = []
ans = 0
count = 0
n = int(input())


def canleft(i, count):
    global x, h, left, right
    for j in x:
        if x[i]-h[i] <= j < x[i]:
            return False
    for j in range(count):
        if not (left[j] > x[i] or right[j] < x[i]-h[i]):
            return False
    return True


def canright(i, count):
    global x, h, left, right
    for j in x:
        if x[i] < j <= x[i]+h[i]:
            return False
    for j in range(count):
        if not (left[j] > x[i]+h[i] or right[j] < x[i]):
            return False
    return True


for i in range(n):
    xi, hi = map(int, input().split())
    x.append(xi)
    h.append(hi)
back = False
i = 0
while True:
    if i == n:
        if count > ans:
            ans = count
        else:
            i -= 1
            back = True
            if cut[-1] != 0:
                count -= 1
                left.pop()
                right.pop()
            cut.pop()
    elif back:
        if len(cut) == 0:
            break
        back = False
        if cut[-1] == 0:
            i -= 1
            back = True
            cut.pop()
        elif cut[-1] == -1:
            if canright(i, count):
                count += 1
                cut[-1] = 1
                left.append(x[i])
                right.append(x[i]+h[i])
                i += 1
            else:
                count -= 1
                i += 1
                cut[-1] = 0
        else:
            count -= 1
            i += 1
            cut[-1] = 0
    else:
        if canleft(i, count):
            count += 1
            cut.append(-1)
            left.append(x[i]-h[i])
            right.append(x[i])
            i += 1
        elif canright(i, count):
            count += 1
            cut.append(1)
            left.append(x[i])
            right.append(x[i]+h[i])
            i += 1
        else:
            i += 1
            cut.append(0)
print(ans)
