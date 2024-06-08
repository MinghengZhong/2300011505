t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    s = input()
    aaa = 0
    for a in s:
        if a == '+':
            aaa += 1
        else:
            aaa -= 1
    ans[_] = abs(aaa)
for a in ans:
    print(a)
