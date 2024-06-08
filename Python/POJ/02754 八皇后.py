count = 0
ans = []


def dp(i, a, b, c, m):
    global ans, count
    if i == 8:
        count += 1
        ans.append(m)
    else:
        for j in range(8):
            if a[j] and b[i+j] and c[i-j+7]:
                a[j] = False
                b[i+j] = False
                c[i-j+7] = False
                m += str(j+1)
                dp(i+1, a, b, c, m)
                m = m[:-1]
                c[i-j+7] = True
                b[i+j] = True
                a[j] = True
    return


dp(0, [True]*8, [True]*15, [True]*15, '')
t = int(input())
for _ in range(t):
    print(ans[int(input())-1])
