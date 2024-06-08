t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    s = list(input())
    sub = []
    for i in range(n):
        while sub and s[sub[-1]] < s[i]:
            sub.pop()
        sub.append(i)
    i = 0
    while i < len(sub) and s[sub[i]] == s[sub[0]]:
        i += 1
    ans[_] = len(sub)-i
    for i in range(len(sub)//2):
        s[sub[i]], s[sub[len(sub)-i-1]] = s[sub[len(sub)-i-1]], s[sub[i]]
    for i in range(1, n):
        if s[i] < s[i-1]:
            ans[_] = -1
            break
for a in ans:
    print(a)
