def F():
    l = sorted([input() for _ in range(int(input()))])
    for i in range(1, len(l)):
        if len(l[i-1]) <= len(l[i]) and l[i-1] == l[i][:len(l[i-1])]:
            return 'NO'
    return 'YES'


for _ in range(int(input())):
    print(F())
