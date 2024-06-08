n = 0
count = 0
ans = ''
l = []
used = []
num = 0


def fence():
    global n, used, num, count, ans
    if ans != '':
        return
    elif num == n:
        if count == 1:
            ans = (' ').join(list(map(str, l)))
            return
        else:
            count -= 1
            return
    else:
        for i in range(1, n+1):
            if (not used[i-1]) and ((num <= 1) or (num > 1 and ((i > l[-1] and l[-2] > l[-1]) or (i < l[-1] and l[-2] < l[-1])))):
                l.append(i)
                used[i-1] = True
                num += 1
                fence()
                l.pop()
                used[i-1] = False
                num -= 1
        return


N = int(input())
for j in range(N):
    n, count = map(int, input().split())
    l = []
    used = [False]*n
    ans = ''
    num = 0
    fence()
    print(ans)
