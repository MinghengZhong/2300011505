n, k = map(int, input().split())
l = sorted(list(map(int, input().split())))
if k == n:
    print(l[-1] if l[-1] <= 1e9 else -1)
elif 0 < k < n:
    if l[k-1] == l[k] or l[k] <= 1:
        print(-1)
    else:
        print(max(1, l[k-1]))
elif k == 0:
    print(1 if l[0] > 1 else -1)
else:
    print(-1)
