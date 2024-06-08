L = int(input())+1
n = int(input())
if n == 0:
    print('0 0')
else:
    l = list(map(int, input().split()))
    ans1 = 0
    ans2 = L
    for a in l:
        b = min(a, L-a)
        if b > ans1:
            ans1 = b
        if b < ans2:
            ans2 = b
    print('%d %d' % (ans1, L-ans2))
