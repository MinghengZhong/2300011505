t = int(input())
ans = [True]*t


def check(a, b):
    if a == 'R':
        return b == 'R'
    else:
        return b != 'R'


for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    for i in range(n):
        if not check(s1[i], s2[i]):
            ans[_] = False
            break
for a in ans:
    if a:
        print('YES')
    else:
        print('NO')
