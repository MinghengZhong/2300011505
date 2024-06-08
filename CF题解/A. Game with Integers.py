t = int(input())
ans = [True]*t
for _ in range(t):
    n = int(input())
    if n % 3 == 0:
        ans[_] = False
for a in ans:
    if a:
        print('First')
    else:
        print('Second')
