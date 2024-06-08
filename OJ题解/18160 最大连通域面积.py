def dfs(i, j):
    global l, used
    count = 1
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if l[x][y] == 'W' and not used[x][y]:
                used[x][y] = True
                count += dfs(x, y)
    return count


t = int(input())
anss = []
for _ in range(t):
    n, m = map(int, input().split())
    used = [[False]*(m+2) for i in range(n+2)]
    l = ['.'*(m+2)]
    ans = 0
    for i in range(n):
        l.append('.'+input()+'.')
    l.append('.'*(m+2))
    for i in range(1, n+1):
        for j in range(1, m+1):
            if l[i][j] == 'W' and not used[i][j]:
                used[i][j] = True
                ans = max(ans, dfs(i, j))
    anss.append(ans)
for ans in anss:
    print(ans)
