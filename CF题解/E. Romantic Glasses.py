for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if i % 2 == 1:
            a[i] = -a[i]
    s = set([0])
    count = 0
    ans = False
    for aa in a:
        count += aa
        if count in s:
            ans = True
            break
        s.add(count)
    if ans:
        print('YES')
    else:
        print('NO')
