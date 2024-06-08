def f(a, b, c, I, J, K):
    if K == len(c):
        return 1
    k = 0
    while I+k-len(a) and J+k-len(b) and a[I+k] == b[J+k] == c[K+k]:
        k += 1
    if k:
        return f(a, b, c, I+k, J, K+k)+f(a, b, c, I, J+k, K+k)
    else:
        if I-len(a) and a[I] == c[K]:
            return f(a, b, c, I+1, J, K+1)
        elif J-len(b) and b[J] == c[K]:
            return f(a, b, c, I, J+1, K+1)
        else:
            return 0


for _ in range(int(input())):
    a, b, c = input().split()
    ans = 0
    if len(c) == len(a)+len(b):
        ans = f(a, b, c, 0, 0, 0)
    print('Data set %d: %s' % (_+1, 'yes' if ans else 'no'))
