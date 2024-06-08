def suf(pre, mid):
    if len(pre) > 1:
        root = pre[0]
        n = mid.index(root)
        left = suf(pre[1:n+1], mid[:n])
        right = suf(pre[n+1:], mid[n+1:])
        return left+right+root
    else:
        return pre


while True:
    try:
        pre = input()
        mid = input()
    except EOFError:
        break
    print(suf(pre, mid))
