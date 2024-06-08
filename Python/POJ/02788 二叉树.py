from math import log, pow
while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    k = int(log(n/m, 2))
    nn = m
    for i in range(k):
        nn = nn*2+1
    n = min(n, nn)
    print(int(pow(2, k)+n-m*pow(2, k)))
