from copy import deepcopy


def right(M):
    global m, n
    changed = False
    while True:
        c = False
        for i in range(m):
            for j in range(n-1):
                if M[i][j] > 0 and M[i][j+1] == 0:
                    M[i][j], M[i][j+1] = 0, M[i][j]
                    c = True
        changed = c
        if not c:
            break
    for i in range(m):
        for j in range(n-1):
            if M[i][j] == M[i][j+1]:
                M[i][j+1] *= 2
                M[i][j] = 0
                changed = True
    while True:
        c = False
        for i in range(m):
            for j in range(n-1):
                if M[i][j] > 0 and M[i][j+1] == 0:
                    M[i][j], M[i][j+1] = 0, M[i][j]
                    c = True
        if not c:
            break
    return changed


def left(M):
    global m, n
    changed = False
    while True:
        c = False
        for i in range(m):
            for j in range(n-1, 0, -1):
                if M[i][j] > 0 and M[i][j-1] == 0:
                    M[i][j], M[i][j-1] = 0, M[i][j]
                    c = True
        changed = c
        if not c:
            break
    for i in range(m):
        for j in range(n-1, 0, -1):
            if M[i][j] == M[i][j-1]:
                M[i][j-1] *= 2
                M[i][j] = 0
                changed = True
    while True:
        c = False
        for i in range(m):
            for j in range(n-1, 0, -1):
                if M[i][j] > 0 and M[i][j-1] == 0:
                    M[i][j], M[i][j-1] = 0, M[i][j]
                    c = True
        if not c:
            break
    return changed


def down(M):
    global m, n
    changed = False
    while True:
        c = False
        for j in range(n):
            for i in range(m-1):
                if M[i][j] > 0 and M[i+1][j] == 0:
                    M[i][j], M[i+1][j] = 0, M[i][j]
                    c = True
        changed = c
        if not c:
            break
    for j in range(n):
        for i in range(m-1):
            if M[i][j] == M[i+1][j]:
                M[i+1][j] *= 2
                M[i][j] = 0
                changed = True
    while True:
        c = False
        for j in range(n):
            for i in range(m-1):
                if M[i][j] > 0 and M[i+1][j] == 0:
                    M[i][j], M[i+1][j] = 0, M[i][j]
                    c = True
        if not c:
            break
    return changed


def up(M):
    global m, n
    changed = False
    while True:
        c = False
        for j in range(n):
            for i in range(m-1, 0, -1):
                if M[i][j] > 0 and M[i-1][j] == 0:
                    M[i][j], M[i-1][j] = 0, M[i][j]
                    c = True
        changed = c
        if not c:
            break
    for j in range(n):
        for i in range(m-1, 0, -1):
            if M[i][j] == M[i-1][j]:
                M[i-1][j] *= 2
                M[i][j] = 0
                changed = True
    while True:
        c = False
        for j in range(n):
            for i in range(m-1, 0, -1):
                if M[i][j] > 0 and M[i-1][j] == 0:
                    M[i][j], M[i-1][j] = 0, M[i][j]
                    c = True
        if not c:
            break
    return changed


def move(M, step):
    global ans
    ans.append(max(max(l) for l in M))
    if step == 0:
        return
    newM = deepcopy(M)
    if right(newM):
        move(newM, step-1)
    newM = deepcopy(M)
    if left(newM):
        move(newM, step-1)
    newM = deepcopy(M)
    if down(newM):
        move(newM, step-1)
    newM = deepcopy(M)
    if up(newM):
        move(newM, step-1)
    return


m, n, p = map(int, input().split())
M, ans = [], []
for _ in range(m):
    M.append(list(map(int, input().split())))
move(M, p)
print(max(ans))
