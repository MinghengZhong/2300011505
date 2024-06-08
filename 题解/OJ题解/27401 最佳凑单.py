n, t = map(int, input().split())
l = sorted(list(map(int, input().split())), reverse=True)
count = sum(l)-t
if count < 0:
    print(0)
else:
    ans = [count]*(n+1)
    start = 0
    while l[start] > count:
        start += 1
        if start == n:
            break
    for i in range(start, n):
        minn = count
        for j in range(start, i):
            if ans[j] >= l[i]:
                minn = min(ans[j], minn)
        ans[i] = minn-l[i]
    print(min(ans)+t)
