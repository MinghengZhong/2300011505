from sys import exit


def dfs(step, goal, count):
    global minn, maxn, num
    if step == 0:
        print(goal)
        exit()
    if count == goal:
        dfs(step-1, goal, 0)
        return
    for i in range(maxn, minn-1, -1):
        if num[i] > 0 and count+i <= goal:
            num[i] -= 1
            dfs(step, goal, count+i)
            num[i] += 1
            if count == 0 or count+i == goal:
                return


n = int(input())
num = [0]*51
l = list(map(int, input().split()))
s, minn, maxn = 0, 51, 0
for a in l:
    if a <= 50:
        s += a
        num[a] += 1
        minn = min(minn, a)
        maxn = max(maxn, a)
ifans = False
for i in range(minn, s//2+1):
    if s % i == 0:
        dfs(s//i, i, 0)
print(s)
