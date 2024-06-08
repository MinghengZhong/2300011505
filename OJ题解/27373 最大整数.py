def bigger(a, b):
    return a+b > b+a


def Sorted(l):
    if len(l) <= 1:
        return l
    mid = l[len(l)//2]
    left, middle, right = [], [], []
    for a in l:
        if a == mid:
            middle.append(a)
        elif bigger(a, mid):
            left.append(a)
        else:
            right.append(a)
    return Sorted(left)+middle+Sorted(right)


m = int(input())
n = int(input())
l = Sorted(input().split())
dp = ['']*(m+1)
for i in range(n):
    ll = len(l[i])
    for j in range(m, ll-1, -1):
        if not dp[j] or int(dp[j-ll]+l[i]) > int(dp[j]):
            dp[j] = dp[j-ll]+l[i]
print(dp[m])
