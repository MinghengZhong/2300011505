t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if max(a) == min(a):
        print(n//2)
    else:
        a.sort()
        if n % 2 == 0:
            i = n//2-1
            j = n//2
        else:
            i = j = n//2
        while True:
            if a[i] != a[i+1]:
                A = i+1
                break
            elif a[j] != a[j-1]:
                A = j
                break
            else:
                i += 1
                j -= 1
        print(A*(n-A))
