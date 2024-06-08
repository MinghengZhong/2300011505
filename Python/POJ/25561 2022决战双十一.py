def dfs(step, memory):
    global M, dis, ans, n, m
    if step == n+1:
        count = sum(memory)
        count -= (count//300)*50
        for i in range(1, m+1):
            for a in dis[i]:
                if a[0] <= memory[i]:
                    count -= a[1]
                    break
        if ans == -1 or count < ans:
            ans = count
    else:
        for i in range(1, m+1):
            if M[step][i] != -1:
                memory[i] += M[step][i]
                dfs(step+1, memory)
                memory[i] -= M[step][i]
    return


n, m = map(int, input().split())
M = [[-1]*(m+1) for i in range(n+1)]
ans = -1
for _ in range(1, n+1):
    inp = input().split()
    for a in inp:
        s, p = map(int, a.split(':'))
        M[_][s] = p
dis = [[]]
for _ in range(1, m+1):
    dis.append([])
    inp = input().split()
    for a in inp:
        q, x = map(int, a.split('-'))
        dis[_].append((q, x))
    dis[_].sort(key=lambda x: x[1], reverse=True)
dfs(1, [0]*(m+1))
print(ans)
