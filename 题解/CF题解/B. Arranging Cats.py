for _ in range(int(input())):
    n = int(input())
    s = input()
    f = input()
    a, b = 0, 0
    for i in range(n):
        if s[i] > f[i]:
            a += 1
        elif s[i] < f[i]:
            b += 1
    print(max(a, b))
