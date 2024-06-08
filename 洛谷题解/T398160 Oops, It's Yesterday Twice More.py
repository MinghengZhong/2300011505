n, a, b = map(int, input().split())
ans = []
if a <= n//2:
    ans += ['U']*(n-1)
    i = 1
else:
    ans += ['D']*(n-1)
    i = n
if b <= n//2:
    ans += ['L']*(n-1)
    j = 1
else:
    ans += ['R']*(n-1)
    j = n
if i >= a:
    ans += ['U']*(i-a)
else:
    ans += ['D']*(a-i)
if j >= b:
    ans += ['L']*(j-b)
else:
    ans += ['R']*(b-j)
print(''.join(ans))
