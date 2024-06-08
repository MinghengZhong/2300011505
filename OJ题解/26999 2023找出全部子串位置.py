N = int(input())


def buildnext(pat):
    next = [0]
    l = 0
    r = 1
    while r < len(pat):
        if pat[l] == pat[r]:
            l += 1
            r += 1
            next.append(l)
        elif l != 0:
            l = next[l-1]
        else:
            r += 1
            next.append(0)
    return next


def search(txt, pat, next):
    ans = []
    i = 0
    j = 0
    while i < len(txt):
        if txt[i] == pat[j]:
            i += 1
            j += 1
        elif j != 0:
            j = next[j-1]
        else:
            i += 1
        if j == len(pat):
            ans.append(i-j)
            j = next[j-1]
    return ans


for _ in range(N):
    txt, pat = input().split()
    ans = search(txt, pat, buildnext(pat))
    if ans == []:
        print('no')
    else:
        print(' '.join(map(str, ans)))
