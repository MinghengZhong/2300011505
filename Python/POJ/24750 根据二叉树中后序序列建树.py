def pre(mid, suf):
    if len(mid) > 1:
        root = suf[-1]
        n = mid.index(root)
        left = pre(mid[:n], suf[:n])
        right = pre(mid[n+1:], suf[n:-1])
        return root+left+right
    else:
        return mid


mid = input()
suf = input()
print(pre(mid, suf))
