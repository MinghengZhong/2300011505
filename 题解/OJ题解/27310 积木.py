n = int(input())
l = [[False]*26 for i in range(4)]


def check(s, step, used):
    global l, ans
    if step == len(s):
        ans = True
        return
    for i in range(4):
        if not used[i] and l[i][ord(s[step])-65]:
            used[i] = True
            check(s, step+1, used)
            used[i] = False
            if ans:
                break
    return


for i in range(4):
    s = input()
    ss = set()
    for a in s:
        ss.add(a)
    for a in ss:
        l[i][ord(a)-65] = True
for i in range(n):
    news = input()
    ans = False
    check(news, 0, [False]*4)
    if ans:
        print('YES')
    else:
        print('NO')
