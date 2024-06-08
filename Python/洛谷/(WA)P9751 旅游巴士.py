u = []
v = []
a = []
n = 0
m = 0
k = 0
ans = -1


def walk(now, step, start, used):
    global u, v, a, m, ans
    if now == n:
        if step % k == 0:
            if start % k == 0:
                new_ans = start+step
            else:
                new_ans = (start//k+1)*k+step
            if ans == -1 or ans > new_ans:
                ans = new_ans
        return
    for i in range(m):
        if u[i] == now and not used[i]:
            if a[i]-step+1 > start:
                used[i] = True
                walk(v[i], step+1, a[i]-step+1, used)
                used[i] = False
            else:
                used[i] = True
                walk(v[i], step+1, start, used)
                used[i] = False


n, m, k = map(int, input().split())
for _ in range(m):
    l = list(map(int, input().split()))
    u.append(l[0])
    v.append(l[1])
    a.append(l[2])
walk(1, 0, 0, [False]*m)
print(ans)
