M = []


def dfs(N, k, I, J):
    global M
    if not k:
        return 1
    if len(M)-N < k:
        return 0
    n = 0
    for i in range(N, len(M)):
        x, y = M[i]
        if I[x] and J[y]:
            I[x] = J[y] = 0
            n += dfs(i+1, k-1, I, J)
            I[x] = J[y] = 1
    return n


while True:
    n, k = map(int, input().split())
    if n == -1:
        break
    M = []
    for i in range(n):
        s = input()
        for j in range(n):
            if s[j] == '#':
                M.append((i, j))
    print(dfs(0, k, [1]*n, [1]*n))
