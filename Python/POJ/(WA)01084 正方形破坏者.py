from collections import Counter as C
from copy import deepcopy
ans = 0


def F(i, j, k, n):
    a = 1+i*(2*n+1)+j
    s = set()
    for _ in range(k):
        s |= set([a+_, a+_+k*(2*n+1), a+_*(2*n+1)+n, a+_*(2*n+1)+n+k])
    return s


def dfs(L, S, x):
    global ans
    if x >= ans:
        return
    if S:
        c = C()
        for i in S:
            c += C(L[i])
        l = sorted(c.keys(), key=lambda x: -c[x])
        if c[l[0]] == 1:
            ans = min(ans, x+len(S))
        else:
            for a in l:
                if c[a] == c[l[0]]:
                    SS = deepcopy(S)
                    s = set()
                    for i in S:
                        if a in L[i]:
                            s.add(i)
                    dfs(L, SS-s, x+1)
    if not S:
        ans = min(ans, x)


for _ in range(int(input())):
    n = int(input())
    l = set(map(int, input().split()[1:]))
    S = set()
    L = []
    x = 0
    for k in range(1, n+1):
        for i in range(n-k+1):
            for j in range(n-k+1):
                s = F(i, j, k, n)
                if not s & l:
                    L.append(s)
                    S.add(x)
                    x += 1
    ans = 1e9
    dfs(L, S, 0)
    print(ans)
