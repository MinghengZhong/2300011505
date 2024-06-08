n = int(input())
l = list(map(int, input().split()))
N = int(max(l)**.5)+1
c = [True]*N
for i in range(3, N, 2):
    c[i] = False
c[0] = False
for i in range(3, N+1, 2):
    if c[i-1]:
        j = i
        while j*i <= N:
            c[j*i-1] = False
            j += 2
for i in range(0, n):
    if int(l[i]**.5) != l[i]**.5:
        print('NO')
    else:
        if c[int(l[i]**.5)-1]:
            print('YES')
        else:
            print('NO')
