n = int(input())
l = list(map(int, input().split()))
for a in l:
    for i in range(1, int((a/2)**.5)+1):
        j = (a-i**2)**.5
        if int(j) == j:
            print(bin(a), end=' ')
            print(oct(a), end=' ')
            print(hex(a))
            break
