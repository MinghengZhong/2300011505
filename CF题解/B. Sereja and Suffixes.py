n, m = map(int, input().split())
a = list(map(int, input().split()))
l = [1]
used = [False]*(max(a)+1)
used[a[-1]] = True
for i in range(n-2, -1, -1):
    if not used[a[i]]:
        used[a[i]] = True
        l.append(l[-1]+1)
    else:
        l.append(l[-1])
for _ in range(m):
    print(l[-int(input())])
