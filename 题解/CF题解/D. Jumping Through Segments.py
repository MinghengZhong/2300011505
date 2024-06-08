t = int(input())
ans = [0]*t


def check(l, r, n, k):
    left, right = 0, 0
    for i in range(n):
        left = max(left-k, l[i])
        right = min(right+k, r[i])
        if left > right:
            return False
    return True


for _ in range(t):
    n = int(input())
    mink, maxk = -1, 1000000000
    l, r = [0]*n, [0]*n
    for i in range(n):
        l[i], r[i] = map(int, input().split())
    while maxk-mink > 1:
        k = (mink+maxk)//2
        if check(l, r, n, k):
            maxk = k
        else:
            mink = k
    ans[_] = maxk
for a in ans:
    print(a)
