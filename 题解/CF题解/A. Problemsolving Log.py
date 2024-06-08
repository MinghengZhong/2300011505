t = int(input())
for _ in range(t):
    n = input()
    l = input()
    ans = 0
    s = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = [0]*27
    for a in l:
        count[s.index(a)] += 1
    for i in range(1, 27):
        if count[i] >= i:
            ans += 1
    print(ans)
