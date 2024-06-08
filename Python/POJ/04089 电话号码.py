for _ in range(int(input())):
    n = int(input())
    l = sorted([input() for i in range(n)])
    ans = True
    for i in range(1, n):
        if len(l[i]) >= len(l[i-1]):
            if l[i][:len(l[i-1])] == l[i-1]:
                ans = False
        if not ans:
            break
    print('YES' if ans else 'NO')
