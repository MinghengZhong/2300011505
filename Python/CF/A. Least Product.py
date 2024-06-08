t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    pos, neg, zero = 0, 0, 0
    for a in l:
        if a > 0:
            pos += 1
        elif a < 0:
            neg += 1
        else:
            zero += 1
            break
    if zero == 1:
        print(0)
    else:
        if neg % 2 == 1:
            print(0)
        else:
            print(1)
            print('1 0')
