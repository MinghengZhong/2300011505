from bisect import bisect


def suf(l):
    if len(l) <= 1:
        return l
    n = bisect(l[1:], l[0])+1
    return suf(l[1:n])+suf(l[n:])+[l[0]]


n = int(input())
l = list(map(int, input().split()))
print(' '.join(map(str, suf(l))))
