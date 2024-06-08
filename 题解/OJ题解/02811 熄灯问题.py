M = [[0]*8]
for _ in range(5):
    M.append([0]+list(map(int, input().split()))+[0])
M.append([0]*8)
ans = [[0]*8 for i in range(7)]
for k in range(64):
    for i in range(1, 6):
        ans[i][1] = k % 2
        k //= 2
    for i in range(2, 7):
        for j in range(1, 6):
            ans[j][i] = (ans[j][i-1]+ans[j-1][i-1]+ans[j+1]
                         [i-1]+ans[j][i-2]+M[j][i-1]) % 2
    b = True
    for i in range(1, 6):
        if M[i][6] != (ans[i][6]+ans[i][5]+ans[i-1][6]+ans[i+1][6]) % 2:
            b = False
            break
    if b:
        for i in range(1, 6):
            print(' '.join(map(str, ans[i][1:-1])))
        break
