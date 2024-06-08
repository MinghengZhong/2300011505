def check(X, Y):
    if X[0] == Y[0] or X[-1] == Y[-1]:
        return False
    elif X[0] > Y[0]:
        if X[-1] < Y[-1]:
            return False
        i = 0
        j = 1
        while (j != len(Y)):
            if X[i] > Y[j]:
                j += 1
            else:
                current = X[i]
                while X[i] == current:
                    i += 1
                if X[i] > Y[j]:
                    j += 1
                else:
                    return False
        return True
    else:
        if X[-1] > Y[-1]:
            return False
        i = 0
        j = 1
        while (j != len(Y)):
            if X[i] < Y[j]:
                j += 1
            else:
                current = X[i]
                while X[i] == current:
                    i += 1
                if X[i] < Y[j]:
                    j += 1
                else:
                    return False
        return True


c, n, m, q = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
ans = ''
if check(X, Y):
    ans += '1'
else:
    ans += '0'
for _ in range(q):
    newX = X.copy()
    newY = Y.copy()
    kx, ky = map(int, input().split())
    for __ in range(kx):
        p, v = map(int, input().split())
        newX[p-1] = v
    for __ in range(ky):
        p, v = map(int, input().split())
        newY[p-1] = v
    if check(X, Y):
        ans += '1'
    else:
        ans += '0'
print(ans)
