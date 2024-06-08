def num(s):
    global dic
    return dic[s]


dic = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
       'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
t = int(input())
anss = []
for _ in range(t):
    n = int(input())
    l = []
    ans = 0
    for i in range(n):
        l.append(tuple(map(num, input())))
    for i in range(n//2):
        for j in range(n//2):
            ans += 4*max(l[i][j], l[j][n-i-1], l[n-i-1][n-j-1], l[n-j-1][i]) - \
                (l[i][j] + l[j][n-i-1] + l[n-i-1][n-j-1] + l[n-j-1][i])
    anss.append(ans)
for ans in anss:
    print(ans)
