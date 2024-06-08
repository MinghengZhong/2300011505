def run(step, n, runned, memory):
    global l, r, V, k
    if step == n:
        check(n, runned, memory)
        return
    run(step+1, n, runned, memory)
    new_memory = memory.copy()
    new_runned = runned.copy()
    new_memory[step] = True
    for i in range(l[step], r[step]+1):
        new_runned[i] = True
    run(step+1, n, new_runned, new_memory)
    return


def check(n, runned, memory):
    global ans, V, k, d
    count = 0
    new_ans = 0
    for a in runned:
        if a:
            count += 1
            new_ans -= d
            if count > k:
                return
        else:
            count = 0
    for i in range(n):
        if memory[i]:
            new_ans += V[i]
    if new_ans > ans:
        ans = new_ans
    return


c, t = map(int, input().split())
for _ in range(t):
    n, m, k, d = map(int, input().split())
    l = []
    r = []
    V = []
    ans = -n*d
    for __ in range(m):
        x, y, v = map(int, input().split())
        if y <= k:
            l.append(x-y+1)
            r.append(x)
            V.append(v)
    N = len(V)
    run(0, N, [False]*(n+1), [False]*N)
    print(ans)
