t = int(input())
anss = []
for _ in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    ans = max(l[0], n-l[-1]+1)
    for i in range(1, k):
        ans = max(ans, (l[i]-l[i-1]+2)//2)
    anss += [ans]
for ans in anss:
    print(ans)
