n = int(input())
l = list(map(int, input().split()))
for i in range(n):
    ans = True
    if int(l[i]**.5) != l[i]**.5 or l[i] < 4:
        ans = False
    elif l[i] > 4:
        a = int(l[i]**.5)
        if a % 2 == 0:
            ans = False
        else:
            for i in range(3, int(a**.5)+1, 2):
                if a % i == 0:
                    ans = False
                    break
    if ans:
        print('YES')
    else:
        print('NO')
