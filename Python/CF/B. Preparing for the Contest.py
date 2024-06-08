t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 0:
        for i in range(n, 1, -1):
            print(i, end=' ')
        print(1)
    elif k == 1:
        for i in range(n-1, 0, -1):
            print(i, end=' ')
        print(n)
    else:
        for i in range(n, k+1, -1):
            print(i, end=' ')
        for i in range(1, k+1):
            print(i, end=' ')
        print(k+1)
