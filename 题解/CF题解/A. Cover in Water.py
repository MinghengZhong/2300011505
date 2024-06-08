t = int(input())
for _ in range(t):
    n = int(input())
    l = input().split('#')
    count = 0
    for a in l:
        count += len(a)
        if len(a) >= 3:
            count = 2
            break
    print(count)
