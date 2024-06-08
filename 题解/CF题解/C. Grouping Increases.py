t = int(input())
ans = [0]*t
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    a, b = [n+1], [n+1]
    count = 0
    for c in l:
        if a[-1] >= b[-1]:
            if c > a[-1]:
                count += 1
                b.append(c)
            elif b[-1] < c <= a[-1]:
                a.append(c)
            else:
                b.append(c)
        else:
            if c > b[-1]:
                count += 1
                a.append(c)
            elif a[-1] < c <= b[-1]:
                b.append(c)
            else:
                a.append(c)
    ans[_] = count
for a in ans:
    print(a)
