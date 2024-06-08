N = int(input())
for i in range(0, N):
    print(int(int(input())**(1/2)))

'''
N = int(input())
while N > 0:
    N -= 1
    n = int(input())
    ans = 0
    l = []
    for i in range(0, n+1):
        l.append(True)
    for i in range(2, n+1):
        j = i
        while j <= n:
            if l[j]:
                l[j] = False
            else:
                l[j] = True
            j += i
    for i in range(1, n+1):
        if l[i]:
            ans += 1
    print(ans)
'''
