n = int(input())
ans = [0]*(n+1)
l = [input().split()]
error = False
for i in range(1, n):
    l.append(input().split())
    for s in l[i]:
        if len(s) != 1:
            ans[l[0].index(l[i][0])] += 1
for i in range(1, n):
    for j in range(1, n):
        if len(l[i][j]) == 2:
            if ans[l[0].index(l[i][j][0])]*(n-1)+ans[l[0].index(l[i][j][1])] != ans[l[0].index(l[i][0])]+ans[l[0].index(l[0][j])]:
                error = True
                break
        else:
            if ans[l[0].index(l[i][j])] != ans[l[0].index(l[i][0])]+ans[l[0].index(l[0][j])]:
                error = True
                break
    if error:
        break
if error:
    print('ERROR!')
else:
    for i in range(n-1):
        print(l[0][i+1]+'='+str(ans[i+1]), end='')
        if i != n-2:
            print(' ', end='')
    print('')
    print(n-1)
