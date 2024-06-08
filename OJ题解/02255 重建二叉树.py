def B(a, b):
    if a:
        n = b.index(a[0])
        return B(a[1:n+1], b[:n])+B(a[n+1:], b[n+1:])+a[0]
    else:
        return ''


while True:
    try:
        a, b = input().split()
    except EOFError:
        break
    print(B(a, b))
