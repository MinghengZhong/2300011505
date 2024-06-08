ans = ['1 0 0 0 0 0 0 0', '0 1 0 0 0 0 0 0', '0 0 1 0 0 0 0 0', '0 0 0 1 0 0 0 0',
       '0 0 0 0 1 0 0 0', '0 0 0 0 0 1 0 0', '0 0 0 0 0 0 1 0', '0 0 0 0 0 0 0 1']
count = 0


def dp(i, a, b, c, m):
    global ans, count
    if i == 8:
        count += 1
        print('No. %d' % (count))
        for j in range(8):
            print(ans[m.index(j)])
    else:
        for j in range(8):
            if a[j] and b[i+j] and c[i-j+7]:
                a[j] = False
                b[i+j] = False
                c[i-j+7] = False
                m.append(j)
                dp(i+1, a, b, c, m)
                m.pop()
                a[j] = True
                b[i+j] = True
                c[i-j+7] = True
    return


dp(0, [True]*8, [True]*15, [True]*15, [])
