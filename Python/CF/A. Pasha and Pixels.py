M = []


def check(i, j):
    global M
    if M[i+1][j] and M[i][j+1] and M[i+1][j+1]:
        return True
    elif M[i-1][j] and M[i][j+1] and M[i-1][j+1]:
        return True
    elif M[i-1][j] and M[i][j-1] and M[i-1][j-1]:
        return True
    elif M[i+1][j] and M[i][j-1] and M[i+1][j-1]:
        return True
    else:
        return False


ans = 0
n, m, k = map(int, input().split())
for i in range(n+2):
    M.append([False]*(m+2))
for _ in range(k):
    x, y = map(int, input().split())
    if ans != 0:
        continue
    elif check(x, y):
        ans = _+1
    else:
        M[x][y] = True
print(ans)
