t = int(input())
l = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3,
     2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5]
ans = [1]*t
for _ in range(t):
    for i in range(l[_]):
        ans[_] *= int(input())
for a in ans:
    print(a)
