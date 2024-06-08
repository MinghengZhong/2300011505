t = int(input())
ans = [0]*t
for _ in range(t):
    n, x, y, M = map(int, input().split())
    l = [[0, 0, 0] for i in range(n)]
    for i in range(n):
        l[i] = list(map(int, input().split()))
    l.sort(key=lambda x: x[2])
    T = [[-1, -1] for i in range(n)]
    for i in range(n):
        for j in range(i-1, -1, -1):
            if l[j][0] <= l[i][0] <= l[j][1] and l[i][2]-l[j][2] <= M:
                if T[j][0] != -1 and T[j][1] != -1:
                    T[i][0] = l[i][2]-l[j][2] + \
                        min(l[i][0]-l[j][0]+T[j][0], l[j][1]-l[i][0]+T[j][1])
                elif T[j][0] != -1:
                    T[i][0] = l[i][2]-l[j][2] + l[i][0]-l[j][0]+T[j][0]
                elif T[j][1] != -1:
                    T[i][0] = l[i][2]-l[j][2] + l[j][1]-l[i][0]+T[j][1]
                break
            if l[i][2]-l[j][2] > M:
                break
        for j in range(i-1, -1, -1):
            if l[j][0] <= l[i][1] <= l[j][1] and l[i][2]-l[j][2] <= M:
                if T[j][0] != -1 and T[j][1] != -1:
                    T[i][1] = l[i][2]-l[j][2] + \
                        min(l[i][1]-l[j][0]+T[j][0], l[j][1]-l[i][1]+T[j][1])
                elif T[j][0] != -1:
                    T[i][1] = l[i][2]-l[j][2] + l[i][1]-l[j][0]+T[j][0]
                elif T[j][1] != -1:
                    T[i][1] = l[i][2]-l[j][2] + l[j][1]-l[i][1]+T[j][1]
                break
            if l[i][2]-l[j][2] > M:
                break
        if l[i][2] <= M:
            if T[i][0] == -1:
                T[i][0] = l[i][2]
            if T[i][1] == -1:
                T[i][1] = l[i][2]
    for i in range(n-1, -1, -1):
        if l[i][0] <= x <= l[i][1]:
            if T[i][0] != -1 and T[i][1] != -1:
                ans[_] = y-l[i][2]+min(x-l[i][0]+T[i][0], l[i][1]-x+T[i][1])
            elif T[i][0] != -1:
                ans[_] = y-l[i][2]+x-l[i][0]+T[i][0]
            elif T[i][1] != -1:
                ans[_] = y-l[i][2]+l[i][1]-x+T[i][1]
            break
    if ans[_] == 0 and y <= M:
        ans[_] = y
for anss in ans:
    print(anss)
