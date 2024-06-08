def add(l, n, next, last, count, head, tail):
    l[n] += 1
    if l[n] == 1:
        if count == 1:
            head, tail = n, n
        else:
            if n > tail:
                next[tail], last[n] = n, tail
                tail = n
            elif n < head:
                last[head], next[n] = n, head
                head = n
            else:
                i = head
                while next[i] < n:
                    i = next[i]
                last[next[i]], next[n] = n, next[i]
                next[i], last[n] = n, i
    next[0], last[0] = 0, 0
    return next, last, head, tail


def minus(l, n, next, last, count, head, tail):
    l[n] -= 1
    if l[n] == 0:
        if n == head:
            head = next[n]
        if n == tail:
            tail = last[n]
        next[last[n]], last[next[n]] = next[n], last[n]
        next[n], last[n] = 0, 0
    next[0], last[0] = 0, 0
    return next, last, head, tail


q = int(input())
s, l, r, ll, rr = [True]*q, {}, {}, [0]*q, [0]*q
lnext, llast, rnext, rlast = {}, {}, {}, {}
ans = [False]*q
for i in range(q):
    inp = input().split()
    if inp[0] == '-':
        s[i] = False
    ll[i], rr[i] = int(inp[1]), int(inp[2])
    l[ll[i]], r[rr[i]] = 0, 0
    lnext[ll[i]], rnext[rr[i]] = 0, 0
    llast[ll[i]], rlast[rr[i]] = 0, 0
l[0], r[0] = 0, 0
right, left, count = 1000000001, 0, 0
headl, taill, headr, tailr = 0, 0, 0, 0
for i in range(q):
    if s[i]:
        count += 1
        lnext, llast, headl, taill = add(
            l, ll[i], lnext, llast, count, headl, taill)
        rnext, rlast, headr, tailr = add(
            r, rr[i], rnext, rlast, count, headr, tailr)
    else:
        count -= 1
        lnext, llast, headl, taill = minus(
            l, ll[i], lnext, llast, count, headl, taill)
        rnext, rlast, headr, tailr = minus(
            r, rr[i], rnext, rlast, count, headr, tailr)
    if taill > headr:
        ans[i] = True
for a in ans:
    if a:
        print('YES')
    else:
        print('NO')
