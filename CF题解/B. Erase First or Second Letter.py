t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    s = input()
    dic = {}
    for a in s:
        dic[a] = 0
        ans[_] += len(dic)
for a in ans:
    print(a)
