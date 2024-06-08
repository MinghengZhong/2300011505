N, D = map(int, input().split())
ans = []
used = [False]*N
l = []
for i in range(N):
    l.append(int(input()))
while True:
    temp = []
    for i in range(N):
        if not used[i]:
            if temp == []:
                temp = [l[i]]
                used[i] = True
                min = l[i]
                max = l[i]
            elif l[i] >= max-D and l[i] <= min+D:
                temp.append(l[i])
                used[i] = True
            if l[i] > max:
                max = l[i]
            if l[i] < min:
                min = l[i]
    if temp == []:
        break
    else:
        ans += sorted(temp)
for a in ans:
    print(a)
