def F(s, i):
    n = 0
    a = ''
    while i < len(s):
        v = s[i]
        i += 1
        if v == ']':
            break
        elif v == '[':
            b, i = F(s, i)
            a += b
        elif '0' <= v <= '9':
            n = n*10+int(v)
        else:
            a += v
    return a*n, i


b, i = F('1'+input(), 0)
print(b)
