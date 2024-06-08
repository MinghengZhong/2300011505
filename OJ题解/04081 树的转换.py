S = input()
h = a = b = 0
H = [0]*len(S)
for s in S:
    if s == 'd':
        h += 1
        H[h] = H[h-1]+1
        a = max(a, h)
        b = max(b, H[h])
    else:
        h -= 1
        H[h] += 1
print('%d => %d' % (a, b))
