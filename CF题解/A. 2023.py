for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    aa = 1
    for i in l:
        aa *= i
    if 2023 % aa == 0:
        print('YES')
        print(2023//aa, end='')
        for i in range(1, k):
            print(' 1', end='')
        print('')
    else:
        print('NO')
