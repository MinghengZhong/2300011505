n = int(input())
inp = [i[1:-1] for i in input().split()]
s = [sum(map(int, inp[i].split(','))) for i in range(n)]
inp = list(map(int, input().split()))
l = [inp[i] for i in range(n)]
for i in range(n):
    s[i] = s[i]/l[i]
ss = sorted(s)
ll = sorted(l)
if n % 2 == 0:
    mids = (ss[n//2-1]+ss[n//2])/2
    midl = (ll[n//2-1]+ll[n//2])/2
else:
    mids = ss[n//2]
    midl = ll[n//2]
ans = 0
for i in range(n):
    if s[i] > mids and l[i] < midl:
        ans += 1
print(ans)
