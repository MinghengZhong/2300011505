def sort(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(n):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
                count += 1
    return count


N = int(input())
anss = []
for _ in range(N):
    n = int(input())
    l = list(map(int, input().split()))
    ans = []
    ll = []
    for a in l:
        ll.append(a)
        ans.append(str(sort(ll)))
    anss.append(' '.join(ans))
