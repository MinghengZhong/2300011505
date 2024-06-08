L, n, m = map(int, input().split())
l = [0]*(n+2)
for i in range(n):
    l[i+1] = int(input())
l[-1] = L


def check(x):
    count = 0
    now = 0
    for i in range(1, n+2):
        if l[i]-now < x:
            count += 1
        else:
            now = l[i]
    return count > m


i = 0
j = L+1
ans = 0
while i < j:
    mid = (i+j)//2
    if check(mid):
        j = mid
    else:
        ans = mid
        i = mid+1
print(ans)
