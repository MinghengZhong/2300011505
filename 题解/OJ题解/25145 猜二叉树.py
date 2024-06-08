from collections import defaultdict as D
ans = D(str)


def build(mid, suf, h):
    global ans
    if not mid:
        return
    root = suf[-1]
    ans[h] += root
    n = mid.index(root)
    build(mid[:n], suf[:n], h+1)
    build(mid[n+1:], suf[n:-1], h+1)


for _ in range(int(input())):
    mid = input()
    suf = input()
    ans = D(str)
    build(mid, suf, 0)
    for i in range(max(ans.keys())+1):
        print(ans[i], end='')
    print('')
