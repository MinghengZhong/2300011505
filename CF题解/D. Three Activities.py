def maxf(a, b, c, la, lb, lc):
    global ans
    used = [la[0]]
    count = a[la[0]]
    if lb[0] not in used:
        count += b[lb[0]]
        used.append(lb[0])
    else:
        count += b[lb[1]]
        used.append(lb[1])
    if lc[0] not in used:
        count += c[lc[0]]
    elif lc[1] not in used:
        count += c[lc[1]]
    else:
        count += c[lc[2]]
    ans = max(count, ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    la = sorted(range(n), key=lambda x: a[x], reverse=True)
    lb = sorted(range(n), key=lambda x: b[x], reverse=True)
    lc = sorted(range(n), key=lambda x: c[x], reverse=True)
    ans = 0
    maxf(a, b, c, la, lb, lc)
    maxf(a, c, b, la, lc, lb)
    maxf(b, a, c, lb, la, lc)
    maxf(b, c, a, lb, lc, la)
    maxf(c, a, b, lc, la, lb)
    maxf(c, b, a, lc, lb, la)
    print(ans)
