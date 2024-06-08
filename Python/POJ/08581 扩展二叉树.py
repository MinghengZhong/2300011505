def F(s, k):
    if len(s) == 1:
        return ''
    i, c = 1, 2
    while c-1:
        c -= 2*int(s[i] == '.')-1
        i += 1
    l = F(s[1:i], k)
    r = F(s[i:], k)
    if k:
        return l+r+s[0]
    else:
        return l+s[0]+r


s = input()
print(F(s, 0))
print(F(s, 1))
