N = int(input())
n = int(((1+8*N)**.5-1)/2)
k = N-int(n*(n+1)/2)
if k == 0:
    k = n
    n -= 1
if n % 2 == 1:
    print('%d/%d' % (k, n-k+2))
else:
    print('%d/%d' % (n-k+2, k))
