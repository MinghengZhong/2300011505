for _ in range(int(input())):
    n = int(input())
    ans, b, l = [2**30-1]*n, True, [[]]*n
    for i in range(n):
        l[i] = list(map(int, input().split()))
        for j in range(i+1, n):
            ans[i] &= l[i][j]
            ans[j] &= l[i][j]
    for i in range(n-1):
        for j in range(i+1, n):
            if ans[i] | ans[j] != l[i][j]:
                b = False
                break
        if not b:
            break
    if b:
        print('YES')
        for i in range(n-1):
            print(ans[i], end=' ')
        print(ans[-1])
    else:
        print('NO')
