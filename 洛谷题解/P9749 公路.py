n, d = map(int, input().split())
v = list(map(int, input().split()))
a = list(map(int, input().split()))
p = a[0]
ans = 0
dis = 0
last = 0
for i in range(1, n):
    dis += v[i-1]
    if a[i] < p and i != n-1:
        if (dis-last) <= 0:
            last -= dis
            p = a[i]
            dis = 0
        else:
            if (dis-last) % d == 0:
                lastL = (dis-last)//d
                last = 0
            else:
                lastL = (dis-last)//d+1
                last += lastL*d-dis
            ans += lastL*p
            p = a[i]
            dis = 0
if last < dis:
    if (dis-last) % d == 0:
        lastL = (dis-last)//d
        last = 0
    else:
        lastL = (dis-last)//d+1
        last += lastL*d-dis
    ans += lastL*p
print(ans)
